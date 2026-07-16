from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()


model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
)

chat_history = [
    SystemMessage(content="You are a helpful assistant that provides information and answers questions based on the conversation history.")
]  # Initialize an empty list to store chat history

# A simple chatbot with history or contect of previous chat.
while True:
    user_input = input("You:")
    # Append user input to chat history
    chat_history.append(f"You: {HumanMessage(user_input)}")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the chatbot. Goodbye!")
        break
    response = model.invoke(chat_history)
    # Append chatbot response to chat history
    chat_history.append(f"Chatbot: {AIMessage(response.content)}")
    print(f"Chatbot: {response.content}")


"""
Response:
You:hi
Chatbot: <think>
Okay, the user said hi to me. I need to respond appropriately. Let me think about a good greeting.

I should keep it friendly and welcoming. Maybe ask how they're doing. 

I should make sure the tone is positive. Offer help in case they need anything. 

That should cover it. Let me put that together in a natural way.
</think>

Hi there! 😊 How are you doing today? Let me know if there's anything I can help with!
You:Tell me about yourself. What kind of model are you and what do you do?
Chatbot: <think>
Okay, the user asked me to tell them about myself, specifically what kind of model I amand what I do. I need to provide a clear and concise answer.

First, I should mention my name, Qwen, and that I'm a large language model developed byAlibaba Cloud. I need to explain my capabilities, like answering questions, creating text, and supporting multiple languages. Also, I should highlight my training data cutoff date to set accurate expectations. It's important to keep the tone friendly and invite them to ask more questions. Let me structure this information in a natural way without technical jargon. Make sure to cover all the key points they might be interested in and end with an offer to help further.
</think>

I'm Qwen, a large language model developed by Alibaba Cloud. I'm designed to help with a wide range of tasks, such as answering questions, generating text (like writing stories, emails, or documents), translating languages, and engaging in conversations. I can also analyze data, provide explanations, and assist with problem-solving. My training datacutoff date is October 2024, so I can discuss information up to that point. I aim to behelpful, accurate, and respectful in all interactions. How can I assist you today? 😊
You:exit
Exiting the chatbot. Goodbye!
"""