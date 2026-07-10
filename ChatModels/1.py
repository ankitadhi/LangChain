from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

#Higher temperature leads to more creative responses, while lower temperature leads to more deterministic responses.
model = ChatGoogleGenerativeAI(model='gemini-2.5-flash', temperature=1.3)

response = model.invoke("Name of five important events in world history?")

print(response.content)