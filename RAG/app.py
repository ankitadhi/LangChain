import json
import os
import tempfile
import textwrap

import numpy as np
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.output_parsers import JsonOutputParser, StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()


EMBED_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
MODEL = "gemini-2.5-flash"
CHUNK_SIZE = 900
CHUNK_OVERLAP = 150
RETRIEVAL_K = 5

st.set_page_config(page_title="PDF RAG Bot (LangChain)", page_icon="📚", layout="wide")


# --------------------------------------------------------------------------
# Cached resources
# --------------------------------------------------------------------------

@st.cache_resource(show_spinner=False)
def load_embedder():
    return HuggingFaceEmbeddings(model_name=EMBED_MODEL_NAME)


# --------------------------------------------------------------------------
# PDF -> chunks (LangChain loader + splitter)
# --------------------------------------------------------------------------

def load_and_split(uploaded_file, chunk_size: int, chunk_overlap: int) -> list[Document]:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    try:
        loader = PyPDFLoader(tmp_path)
        pages = loader.load()
    finally:
        os.unlink(tmp_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.split_documents(pages)


def build_vectorstore(docs: list[Document], embedder: HuggingFaceEmbeddings) -> FAISS:
    return FAISS.from_documents(docs, embedder)


def format_docs(docs: list[Document]) -> str:
    return "\n\n".join(
        f"[Page {d.metadata.get('page', '?') + 1}]\n{d.page_content}" for d in docs
    )


# --------------------------------------------------------------------------
# LCEL chains
# --------------------------------------------------------------------------

def get_llm(max_output_tokens: int) -> ChatGoogleGenerativeAI:
    return ChatGoogleGenerativeAI(
        model=MODEL,
        google_api_key=st.session_state.api_key,
        max_output_tokens=max_output_tokens,
        temperature=0.3,
    )


QA_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful assistant answering questions about a specific book "
     "using only the provided excerpts. If the excerpts don't contain the "
     "answer, say so honestly instead of guessing. Cite page numbers in "
     "parentheses when relevant."),
    ("human", "Book excerpts:\n\n{context}\n\nQuestion: {question}"),
])

QUIZ_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You write multiple-choice quiz questions strictly grounded in the "
     "given book excerpts. Respond with ONLY valid JSON, no preamble, no "
     "markdown fences. JSON schema:\n"
     '[{{"question": str, "options": [str, str, str, str], '
     '"correct_index": int (0-3), "explanation": str}}]'),
    ("human",
     "Book excerpts:\n\n{context}\n\n"
     "Write {num_questions} {difficulty}-difficulty multiple-choice questions "
     "based only on these excerpts. Each question needs exactly 4 options "
     "with exactly one correct answer. Vary the correct option's position."),
])


def answer_question(question: str, retriever) -> tuple[str, list[Document]]:
    docs = retriever.invoke(question)
    chain = QA_PROMPT | get_llm(800) | StrOutputParser()
    answer = chain.invoke({"context": format_docs(docs), "question": question})
    return answer, docs


def generate_quiz(docs: list[Document], num_questions: int, difficulty: str) -> list[dict]:
    chain = QUIZ_PROMPT | get_llm(2000) | JsonOutputParser()
    return chain.invoke({
        "context": format_docs(docs),
        "num_questions": num_questions,
        "difficulty": difficulty,
    })


# --------------------------------------------------------------------------
# Sidebar: setup
# --------------------------------------------------------------------------

with st.sidebar:
    st.header("Setup")

    st.text_input(
        "Google API key",
        type="password",
        value=os.getenv("GOOGLE_API_KEY", ""),
        help="Not stored anywhere except this session. Get one at aistudio.google.com/apikey",
        key="api_key",
    )

    uploaded = st.file_uploader("Upload a PDF book", type=["pdf"], key="sidebar_pdf_uploader")

    col1, col2 = st.columns(2)
    with col1:
        chunk_size = st.number_input(
            "Chunk size", 300, 2000, CHUNK_SIZE, step=100, key="sidebar_chunk_size"
        )
    with col2:
        chunk_overlap = st.number_input(
            "Overlap", 0, 500, CHUNK_OVERLAP, step=50, key="sidebar_chunk_overlap"
        )

    build_clicked = st.button(
        "Build index", type="primary", use_container_width=True, key="sidebar_build_button"
    )

    if build_clicked:
        if not uploaded:
            st.error("Upload a PDF first.")
        else:
            with st.spinner("Loading, splitting, and embedding with LangChain..."):
                docs = load_and_split(uploaded, chunk_size, chunk_overlap)
                embedder = load_embedder()
                vectorstore = build_vectorstore(docs, embedder)

                st.session_state.docs = docs
                st.session_state.vectorstore = vectorstore
                st.session_state.retriever = vectorstore.as_retriever(
                    search_kwargs={"k": RETRIEVAL_K}
                )
                st.session_state.book_name = uploaded.name
            st.success(f"Indexed {len(docs)} chunks.")

    if "docs" in st.session_state:
        st.caption(f"📖 Loaded: **{st.session_state.book_name}** — {len(st.session_state.docs)} chunks")


# --------------------------------------------------------------------------
# Main area
# --------------------------------------------------------------------------

st.title("📚 PDF RAG Bot — LangChain edition")
st.caption("Upload a book, then ask questions or generate a quiz grounded in its actual content.")

has_key = bool(st.session_state.get("api_key"))
has_index = "retriever" in st.session_state

if not has_key or not has_index:
    missing = []
    if not has_key:
        missing.append("a **Google API key** (sidebar)")
    if not has_index:
        missing.append("a **built index** (upload a PDF and click *Build index*)")
    st.info("Still need: " + " and ".join(missing) + ".")
    st.stop()

tab_ask, tab_quiz = st.tabs(["💬 Ask Questions", "📝 Generate Quiz"])

# ---- Ask Questions tab ----
with tab_ask:
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    question = st.chat_input("Ask something about the book...")
    if question:
        st.session_state.chat_history.append(("user", question))
        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Retrieving relevant passages and thinking..."):
                answer, sources = answer_question(question, st.session_state.retriever)
            st.markdown(answer)
            with st.expander("Sources used"):
                for d in sources:
                    page = d.metadata.get("page", "?")
                    page = page + 1 if isinstance(page, int) else page
                    st.markdown(f"**Page {page}:** {textwrap.shorten(d.page_content, 200)}")

        st.session_state.chat_history.append(("assistant", answer))

# ---- Quiz tab ----
with tab_quiz:
    c1, c2, c3 = st.columns(3)
    with c1:
        num_q = st.slider("Number of questions", 3, 15, 5, key="quiz_num_questions")
    with c2:
        difficulty = st.selectbox(
            "Difficulty", ["easy", "medium", "hard"], index=1, key="quiz_difficulty"
        )
    with c3:
        topic = st.text_input(
            "Focus topic (optional)",
            placeholder="e.g. chapter 3, a character name...",
            key="quiz_focus_topic",
        )

    if st.button("Generate quiz", type="primary", key="quiz_generate_button"):
        with st.spinner("Selecting content and writing questions..."):
            all_docs = st.session_state.docs
            if topic.strip():
                wide_retriever = st.session_state.vectorstore.as_retriever(
                    search_kwargs={"k": min(12, len(all_docs))}
                )
                pool = wide_retriever.invoke(topic)
            else:
                rng = np.random.default_rng()
                sample_size = min(12, len(all_docs))
                idxs = rng.choice(len(all_docs), size=sample_size, replace=False)
                pool = [all_docs[i] for i in idxs]

            try:
                quiz = generate_quiz(pool, num_q, difficulty)
                st.session_state.quiz = quiz
            except (json.JSONDecodeError, ValueError) as e:
                st.error(f"Couldn't parse quiz output, try again. ({e})")

    if "quiz" in st.session_state and st.session_state.quiz:
        with st.form("quiz_form"):
            answers = {}
            for i, q in enumerate(st.session_state.quiz):
                st.markdown(f"**{i + 1}. {q['question']}**")
                answers[i] = st.radio(
                    f"q{i}", q["options"], key=f"quiz_q{i}", label_visibility="collapsed"
                )
                st.write("")
            submitted = st.form_submit_button("Submit answers")

        if submitted:
            score = 0
            for i, q in enumerate(st.session_state.quiz):
                correct_option = q["options"][q["correct_index"]]
                is_correct = answers[i] == correct_option
                score += int(is_correct)
                icon = "✅" if is_correct else "❌"
                st.markdown(f"{icon} **Q{i + 1}:** {q['question']}")
                if not is_correct:
                    st.markdown(f"Your answer: {answers[i]}")
                    st.markdown(f"Correct answer: **{correct_option}**")
                st.caption(q.get("explanation", ""))
                st.write("")
            st.success(f"Score: {score} / {len(st.session_state.quiz)}")