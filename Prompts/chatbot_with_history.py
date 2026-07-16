from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
)

chat_history = []  # Initialize an empty list to store chat history

#A simple chatbot with history or contect of previous chat.
while True:
    user_input = input("You:")
    chat_history.append(f"You: {user_input}")  # Append user input to chat history
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    chat_history.append(f"Chatbot: {response.content}")  # Append chatbot response to chat history
    print(f"Chatbot: {response.content}")
