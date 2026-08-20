from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


store = {}

llm = ChatGroq(
    model='openai/gpt-oss-20b'
)

def get_history(session_id):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful assistant'),
    ('placeholder', '{history}'),
    ('human', '{input}')

])

chain = prompt | llm

chat = RunnableWithMessageHistory(
    chain,
    get_history,
    input_message_key='input',
    history_messages_key='history'
)

cfg = {"configurable": {"session_id": 'user-1'}}
chat.invoke({"input": "My name is Ankit."}, config=cfg)
print(chat.invoke({"input": "What's my name?"}, config=cfg).content)
