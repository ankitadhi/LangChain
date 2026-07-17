from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langchain_core.messages import ChatMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
)
#Use of Message Placeholder in ChatPromptTemplate
chat_template = ChatPromptTemplate([
    ('system', "You are a helpful customer support agent"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human', "{query}")
])

chat_history = []

#Load chat History
with open('chat_history.txt') as f:
    chat_history.extend(f.readlines())

print(chat_history)

#Create Prompt
prompt = chat_template.invoke({
    'chat_history': chat_history,
    'query': HumanMessage(content='Where is my refund?'),
 })

response = model.invoke(prompt)

print(response.content)


""""
Your refund for order #12345 is currently being 
processed and should be completed within 3-5 business
days. To check the latest status, you can also log into
your account on our website and review the order 
details. If you've exceeded the processing time 
window or need further assistance, let us know, 
and we’ll investigate! 😊
"""