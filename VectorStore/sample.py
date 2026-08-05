from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
load_dotenv()

document_loader = TextLoader(
    file_path="./smaple.txt",
    encoding="utf-8")

documents = document_loader.load()

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500, 
    chunk_overlap=50,
    separators=["\n\n", "\n", " ", ""]
)

chunks = splitter.split_documents(documents)

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
    )


vector_store = Chroma.from_documents(
    documents=chunks,
    persist_directory="./chromadb",
    embedding=embeddings
)


results = vector_store.similarity_search(
    "What is the main topic of the document?", 
    k=3)


for result in results:
    print(result.page_content)