import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()  # loads OPENAI_API_KEY from .env

# Initialize the model once (outside the loop, so it's not recreated every turn)
llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.7)

# Keep track of conversation history so the bot has memory
chat_history = [
    SystemMessage(content="You are a helpful assistant.")
]

def generate_response(user_message: str) -> str:
    chat_history.append(HumanMessage(content=user_message))
    response = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    return response.content


def main():
    print("Welcome to the LangChain Chatbot!")

    while True:
        user_message = input("> ")

        if user_message.lower() == "exit":
            print("Goodbye!")
            break

        response = generate_response(user_message)
        print(f"Chatbot: {response}")


if __name__ == "__main__":
    main()