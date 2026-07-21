# 🚀 LangChain Learning Journey

> A structured repository documenting my journey of learning **LangChain** through tutorials, official documentation, and hands-on projects.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-orange?style=flat-square)

---

## 📖 About

This repository contains my notes, code examples, experiments, and mini-projects while learning **LangChain**.

The goal is not only to understand LangChain concepts but also to build practical AI applications using LLMs, Retrieval-Augmented Generation (RAG), agents, memory, tools, and vector databases.

Most examples are implemented from scratch while following various educational resources and then extending them with my own experiments.

---

## 🎯 Learning Goals

- Learn LangChain fundamentals
- Build LLM-powered applications
- Understand Prompt Engineering
- Work with Chat Models
- Learn Output Parsers
- Implement Chains
- Build Retrieval-Augmented Generation (RAG)
- Use Vector Databases
- Implement AI Agents
- Work with Memory
- Build Production-ready AI workflows

---

# 📚 Topics Covered

## 1. LangChain Basics

- Introduction to LangChain
- Installation
- Project Structure
- Environment Variables
- LangChain Expression Language (LCEL)

---

## 2. Models

- OpenAI
- Groq
- Ollama
- HuggingFace
- Gemini

Topics:

- Chat Models
- Completion Models
- Local Models
- Streaming Responses

---

## 3. Prompt Engineering

- Prompt Templates
- Chat Prompt Templates
- Few-shot Prompting
- Partial Prompts
- Prompt Composition

---

## 4. Output Parsers

- String Output Parser
- JSON Parser
- Pydantic Parser
- Structured Output

---

## 5. Chains

- Sequential Chains
- Runnable Chains
- LCEL Pipelines
- Parallel Chains
- Conditional Chains

---

## 6. Memory

- Conversation Buffer
- Window Memory
- Summary Memory
- Message History

---

## 7. Document Loaders

Examples include:

- PDF Loader
- Text Loader
- CSV Loader
- Web Loader
- Directory Loader

---

## 8. Text Splitters

- Character Splitter
- Recursive Splitter
- Markdown Splitter
- Token Splitter

---

## 9. Embeddings

- OpenAI Embeddings
- HuggingFace Embeddings
- Sentence Transformers

---

## 10. Vector Databases

Examples with:

- FAISS
- ChromaDB
- Pinecone
- Weaviate

Topics:

- Similarity Search
- Metadata Filtering
- Semantic Search

---

## 11. Retrieval

- Retriever
- Multi Query Retriever
- Context Compression
- Parent Document Retriever

---

## 12. Retrieval-Augmented Generation (RAG)

Building RAG applications using

- Document Loaders
- Chunking
- Embeddings
- Vector Store
- Retriever
- LLM

---

## 13. Agents

Learning

- Tools
- Agent Executors
- ReAct Agents
- Function Calling
- Tool Calling

---

## 14. Tools

Examples include

- Python Tool
- Calculator
- Search Tool
- Custom Tools
- API Tools

---

## 15. LangSmith

- Tracing
- Debugging
- Evaluation
- Monitoring

---

## 16. LangServe

- Deploying LangChain Apps
- REST APIs

---

## 17. Mini Projects

Examples include:

- 🤖 AI Chatbot
- 📄 PDF Chat
- 📚 Document Q&A
- 📰 News Summarizer
- 🌐 Website Chatbot
- 📧 Email Assistant
- 💻 Code Assistant
- 🧠 Multi-Agent Workflow

---

# 📂 Repository Structure

```
LangChain/
│
├── ChatModels/
├── EmbeddingModels/
├── LLMs/
├── OutputParsers/
├── Prompts/
├── StructuredOutputs/
├── Chains
├── Document_Loaders/
├── Text_Splitters/
├── Vector_Databases/
├── Retrievers/
├── RAG/
├── Agents/
├── Tools/
├── LangSmith/
├── LangServe/
├── Projects/
├── notebooks/
├── assets/
├── requirements.txt
├── .gitignore
├── first.py
├── main.py
└── README.md
```

---

# 🛠️ Tech Stack

- Python
- LangChain
- LangGraph (later)
- OpenAI API
- Google Gemini
- Groq
- Ollama
- HuggingFace
- FAISS
- ChromaDB
- Pinecone
- Streamlit
- FastAPI
- Jupyter Notebook

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/ankitadhi/langchain.git
```

Navigate to the project

```bash
cd langchain-learning
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux / Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
OPENAI_API_KEY=your_key
GOOGLE_API_KEY=your_key
GROQ_API_KEY=your_key
LANGCHAIN_API_KEY=your_key
```

---

# 🚀 Progress

- [x] LangChain Basics
- [x] Prompt Templates
- [x] Models
- [x] Output Parsers
- [ ] Chains
- [ ] Memory
- [ ] Document Loaders
- [ ] Text Splitters
- [x] Embeddings
- [ ] Vector Databases
- [ ] Retrieval
- [ ] RAG
- [ ] Agents
- [ ] LangGraph
- [ ] Production Projects

---

# 📚 Learning Resources

This repository is based on concepts learned from:

- Official LangChain Documentation
- CampusX LangChain Playlist
- LangChain Academy
- DeepLearning.AI Short Courses
- Hugging Face Documentation
- Community blogs, GitHub repositories, and technical articles

The implementations in this repository are recreated, modified, and expanded through hands-on practice and experimentation.

---

# 🤝 Contributions

Suggestions, improvements, and discussions are always welcome.

Feel free to open an issue or submit a pull request.

---

# ⭐ Support

If you find this repository helpful, consider giving it a ⭐ on GitHub.

It motivates me to continue building and sharing AI-related projects.

---

## 📄 License

This project is licensed under the MIT License.
