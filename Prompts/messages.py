from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
)

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content ='Tell Me about LangChain'),
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print("Chat History:")
print("----------------")

for message in messages:
    if isinstance(message, SystemMessage):
        print(f"System: {message.content}")
    elif isinstance(message, HumanMessage):
        print(f"You: {message.content}")
    elif isinstance(message, AIMessage):
        print(f"Chatbot: {message.content}")


"""
Result:
Chat History:
----------------
System: You are a helpful assistant.
You: Tell Me about LangChain
Chatbot: <think>
Okay, the user is asking about LangChain. I should first introduce it as a framework for building AI applications with large language models (LLMs). I need to mention that it was created by Harrison Chase and his team at LangChain. The key features to highlight include integration with LLMs like GPT-3, Hugging Face, or Anthropic, document management for RAG setups, agents for autonomous workflows, memory and state tracking, and the ability to connect with various data sources through tools.

The user might not be familiar with how LangChain helps with different AI application components, so I should explain each feature clearly. For example, document loading and management allows users to process data, and RAG can address LLM limitations. The agent system enables autonomous tasks. I should outline the core concepts like chains, agents, memory, and callbacks.

Additionally, including the components like prompts, models, memory, indexes, and tools will help the user understand its structure. Maybe a simple example with code would clarify how LangChain works. A use case like building a chatbot that connects to a database using LangChain's tools would be good.

I should also mention the benefits such as modular system, easy to use, scalable for different AI applications, and strong community support. The use cases include chatbots, data analysis, content creation, automation workflows, etc.

I should check if there's anything I'm missing, like recent updates or if the user has a specific context in mind. Since the question is general, keeping the response comprehensive but not too technical would be best. Make sure to explain terms like RAG in simple terms.
</think>

**LangChain** is a **framework for building applications powered by large language models (LLMs)** like OpenAI's GPT-3.5/4, Anthropic's Claude, Hugging Face models, and more. It provides tools to streamline tasks such as document processing, question-answering, automation, and conversational AI. Created by Harrison Chase and the LangChain team, it’s become a go-to library for developers leveraging LLMs in production systems.

Here's a breakdown of LangChain's core concepts and features:

---

### **Key Features of LangChain**
1. **Language Model Integration**  
   - LangChain works seamlessly with major LLM providers (e.g., OpenAI, Anthropic, Hugging Face).
   - Provides abstractions for calling models, handling input/output, and managing model parameters.

2. **Document Management (Retrieval Augmented Generation - RAG)**  
   - **Load**: Import documents from various formats (PDFs, CSVs, websites).
   - **Index**: Create vector databases (e.g., FAISS, Pinecone) to store document embeddings.
   - **Retrieval**: Query the index to find relevant documents to enhance LLM answers.

3. **Agents for Autonomy**  
   - **LangChain Agents** act as workflows that decide which tools (code, APIs, databases) to use for a task.
   - Example: An agent can search the web, query a SQL database, or call an API to solve a problem autonomously.

4. **Memory & State Tracking**  
   - Supports short-term, long-term, or conversation history tracking for context-aware interactions.
   - Example: A chatbot can remember a user’s name throughout a conversation.

5. **Tool Integration**  
   - Connects to external services (e.g., APIs, databases, code interpreters) to perform real-world tasks.
   - Example: A chatbot might use a tool to calculate taxes or fetch live stock prices.

6. **Modular Components**  
   - **Chains**: Composable sequences of steps (LLMs, prompts, or other chains).
   - **Agents**: Smart workflows that interact with tools.
   - **Callbacks**: Custom code to log results, track performance, or debug.

---

### **Core Concepts**
- **Prompts**: Templates for generating model inputs (e.g., "Answer this query using the context below:").
- **Models**: LLMs or smaller models for inference or embedding.
- **Memory**: Stores and uses historical data to inform responses.
- **Indexes**: Vector databases for efficient document similarity searches (used in RAG).
- **Tools**: External integrations for specific tasks (e.g., a SQL query tool).
- **Agents**: Combine models, tools, and memory to perform complex tasks autonomously.

---

### **Example Use Case**
> **Building a Q&A Chatbot with RAG**
1. Load a document (e.g., a PDF about machine learning).
2. Create a vector index (e.g., FAISS) to store document embeddings.
3. When a user asks a question, retrieve relevant documents from the index.
4. Use an LLM to generate an answer based on the retrieved context (RAG).

```python
from langchain import OpenAI, PromptTemplate, RetrievalQA
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

# Step 1: Load documents
loader = TextLoader("example.txt")
documents = loader.load()

# Step 2: Split and index
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = FAISS.from_documents(docs, embeddings)

# Step 3: Build a Q&A chain
llm = OpenAI(model_name="gpt-3.5-turbo")
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=db.as_retriever())

# Ask a question
result = qa.run("What is the key takeaway from the text?")
print(result)
```

---

### **Why Use LangChain?**
- **Modular**: Mix and match components for flexibility.
- **Scalable**: Handles complex workflows while staying efficient.
- **Community-Driven**: Expansive libraries, tutorials, and ecosystem (e.g., plugins for GPT-4, Claude).
- **Product-Ready**: Designed for real-world applications (chatbots, data analysis, agents).

---

### **Use Cases**
1. **Chatbots** (e.g., customer support bots with RAG).
2. **Data Analysis**: Automate report generation, insights, or visualizations.
3. **Automation**: Agents for scheduling, code generation, or workflow orchestration.
4. **Education**: Personalized tutoring or knowledge-base Q&A systems.

---

### **Resources**
- **Docs**: [https://python.langchain.com](https://python.langchain.com)
- **GitHub**: [https://github.com/langchain-ai/langchain](https://github.com/langchain-ai/langchain)
- **Community**: Active forums and workshops for troubleshooting.

"""
