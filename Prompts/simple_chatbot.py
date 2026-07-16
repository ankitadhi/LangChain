from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0
    )
# This is a simple chatbot that uses Qwen3-32b model to respond to user inputs. The chatbot will continue to prompt the user for input until the user types "exit" or "quit"
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(user_input)
    print(f"Chatbot: {response.content}")
