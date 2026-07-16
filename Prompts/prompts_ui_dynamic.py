from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate, load_prompt

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

prompt_template = load_prompt("dynamic_prompt_template.json")

# Generate the prompt using the template and user inputs
prompt = prompt_template.format(
    style=style_input, 
    length=summary_length_input, 
    paper_text=paper_input)

if st.button("Generate Summary"):
    result = model.invoke(prompt)
    st.write(result.content)