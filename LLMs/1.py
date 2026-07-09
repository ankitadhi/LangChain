from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash", 
                             temperature=0.7)

#Invoke the model with a prompt

response = llm.invoke("Write a short poem about the beauty of nature.")

print(response.content)
