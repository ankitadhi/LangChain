from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate

load_dotenv()
model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=0,
)

#This is an example of dynamic Prompts

st.header("Dynamic Research Tool")

paper_input = st.text_area("Enter your research paper text here")
style_input = st.selectbox("Select the style of summary", ["Concise", "Detailed", "Bullet Points"])
summary_length_input = st.slider("Choose the length of the summary", min_value=50, max_value=500, value=150)

# Define a prompt template based on user inputs
prompt_template = PromptTemplate(
    template="Summarize the following research paper in a {style} style with a maximum of {length} words:\n\n{paper_text} wtihout any thinking texts",
    input_variables=["style", "length", "paper_text"]
)

# Generate the prompt using the template and user inputs
prompt = prompt_template.format(
    style=style_input, 
    length=summary_length_input, 
    paper_text=paper_input)

if st.button("Generate Summary"):
    result = model.invoke(prompt)
    st.write(result.content)