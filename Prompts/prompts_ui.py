from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


#This is an example of static Prompts

st.header("Research Tool")

user_input = st.text_input("Enter your prompt")

if st.button("Summarize"):
    model = ChatGroq(
        model="qwen/qwen3-32b",
        temperature=0,)
    result = model.invoke(user_input)
    st.text(result.content)