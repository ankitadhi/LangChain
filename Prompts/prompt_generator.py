
from langchain_core.prompts import PromptTemplate

# Define a prompt template based on user inputs
prompt_template = PromptTemplate(
    template="""
    Summarize the following research paper in a {style} style 
    with a maximum of {length} words:\n\n{paper_text} 
    wtihout any thinking texts.
    """,
    input_variables=["style", "length", "paper_text"],
    validate_template=True
)

prompt_template.save("dynamic_prompt_template.json")
