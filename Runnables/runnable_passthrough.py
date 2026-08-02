from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableParallel, RunnableSequence


load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)


prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel(
    {
        "joke": RunnablePassthrough(),
        "explanation": RunnableSequence(
            prompt2, model, parser
        )
    }
)

final_chain = RunnableSequence(joke_gen_chain, parallel_chain,)

print(final_chain.invoke({"topic": "programming"})) 


"""
{'joke': 'Why do programmers prefer dark mode?\n\nBecause light attracts bugs.', 'explanation': 'This joke is a play on words. In the context of programming, "bugs" refers to errors or glitches in the code. Programmers often use the term "bug" to describe these issues.\n\nThe punchline "light attracts bugs" is a clever pun because it sounds similar to the phrase "light attracts bugs" in the context of insects, but in this case, it\'s referring to the coding errors.\n\nThe joke is saying that programmers prefer dark mode (a feature on many digital devices that inverts the colors to make the screen darker) because the word "light" sounds like "bugs," and they\'re trying to avoid attracting coding errors (bugs) to their work. It\'s a lighthearted and humorous way to poke fun at the challenges of programming.'}

"""