from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
import requests
from langchain_core.tools import tool
load_dotenv()


#Create tool
@tool
def multiply(a: int, b: int) -> int:
    """Given 2 numbers a and b this tool returns their product"""

    return a * b


print(multiply.invoke({
  'a': 3,
  'b': 4
}))


llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash-lite'
)

# print(llm.invoke('hi'))

llm_with_tools = llm.bind_tools([multiply])

query = HumanMessage('Can you multiply 3 by 10000?')

messages = [query]

result = llm_with_tools.invoke(messages)

# print(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)

print(messages)


