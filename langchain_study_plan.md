# LangChain Study Plan (4 Weeks, 1–2 hrs/day)
**Goal:** Build production-ready chatbots and RAG (Retrieval-Augmented Generation) apps
**Level:** Intermediate Python, new to LangChain

---

## Week 1 — Foundations & Core Building Blocks

| Day | Time | Topic | What to Do |
|-----|------|-------|-------------|
| 1 | 1.5h | Setup & LLM basics | Install LangChain, set up API keys (OpenAI/Anthropic), run your first `invoke()` call |
| 2 | 1h | Prompt Templates | Learn `PromptTemplate`, `ChatPromptTemplate`, variables, few-shot prompting |
| 3 | 1.5h | LCEL (LangChain Expression Language) | Chain components with `\|` operator, understand Runnables |
| 4 | 1h | Output Parsers | `StrOutputParser`, `PydanticOutputParser`, structured output |
| 5 | 1.5h | Memory basics | `ConversationBufferMemory`, `ConversationSummaryMemory` |
| 6 | 1h | Mini project | Build a simple conversational chatbot (no retrieval yet) |
| 7 | 0.5h | Review & recap | Re-read docs, redo any unclear exercises |

**Milestone:** A working chatbot that remembers conversation history.

---

## Week 2 — Retrieval-Augmented Generation (RAG) Core

| Day | Time | Topic | What to Do |
|-----|------|-------|-------------|
| 8 | 1.5h | Document Loaders | Load PDFs, text files, web pages (`PyPDFLoader`, `WebBaseLoader`) |
| 9 | 1.5h | Text Splitting | `RecursiveCharacterTextSplitter`, chunk size/overlap tradeoffs |
| 10 | 1.5h | Embeddings | OpenAI/HuggingFace embeddings, what vectors represent |
| 11 | 2h | Vector Stores | Set up Chroma or FAISS locally, store & query embeddings |
| 12 | 1.5h | Retrievers | Similarity search, MMR, retriever configuration |
| 13 | 2h | Basic RAG chain | Combine retriever + LLM into a Q&A chain using LCEL |
| 14 | 1h | Review & recap | Rebuild the RAG chain from scratch without looking at notes |

**Milestone:** A working RAG pipeline answering questions over your own documents.

---

## Week 3 — Production RAG & Chatbot Patterns

| Day | Time | Topic | What to Do |
|-----|------|-------|-------------|
| 15 | 1.5h | Conversational RAG | Combine memory + retrieval (history-aware retriever) |
| 16 | 1.5h | Advanced retrieval | Multi-query retriever, contextual compression, re-ranking |
| 17 | 2h | Vector DB upgrade | Try a hosted vector DB (Pinecone, Qdrant, or Weaviate) |
| 18 | 1.5h | Streaming responses | Stream tokens to a UI (important for chatbots) |
| 19 | 1.5h | Evaluation basics | Use LangSmith (or simple manual eval) to test RAG quality |
| 20 | 2h | Project work | Build a RAG chatbot over a real dataset (docs, PDFs, or a website) |
| 21 | 1h | Review & recap | Debug/refine your project |

**Milestone:** A conversational RAG chatbot with memory + streaming.

---

## Week 4 — Agents, Deployment & Polish

| Day | Time | Topic | What to Do |
|-----|------|-------|-------------|
| 22 | 1.5h | Intro to Agents | `create_react_agent`, tool calling basics |
| 23 | 1.5h | Custom Tools | Wrap your RAG retriever as a tool an agent can call |
| 24 | 1.5h | LangGraph intro | Learn why LangGraph exists, basic stateful graph |
| 25 | 1.5h | Error handling | Retries, fallbacks, guardrails for production |
| 26 | 2h | Deployment | Wrap your app with FastAPI or Streamlit for a UI |
| 27 | 2h | Final project polish | Add citations, source display, and clean UX to your RAG app |
| 28 | 1h | Wrap-up | Document your project, write a README, reflect on gaps |

**Milestone:** A deployed, polished RAG chatbot you can show in a portfolio.

---

## Recommended Resources
- **Official docs:** python.langchain.com (always check version — API changes fast)
- **LangChain Academy** (free official courses)
- **LangSmith** for tracing/debugging chains
- **Practice datasets:** your own notes, a company's public docs, or Wikipedia articles

## Tips for Retention
- Rebuild each mini-project from memory before moving to the next week
- Keep a running "gotchas" file — LangChain's API changes often, note what broke and why
- Prefer LCEL syntax over legacy `Chain` classes (like `LLMChain`) — it's the modern standard
