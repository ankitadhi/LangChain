from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()


prompt = PromptTemplate(
    template="Write a  joke about {topic}",
    input_variables=["topic"]
)

prompt1 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt, model, parser, prompt1, model,parser)

result = chain.invoke({"topic": "Chicken"})
print(result)

"""
This is a play on words joke. The punchline "fowl breath" is a pun on the phrase "foul breath," which is a common reason for visiting a doctor. However, "fowl" has a different meaning in this context - it refers to birds, particularly chickens. So, the joke is making a connection between the fact that the chicken is a bird (fowl) and the phrase "fowl breath," creating a humorous and clever play on words."""
