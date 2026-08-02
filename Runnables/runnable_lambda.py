from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableLambda,
    RunnableParallel,
    RunnablePassthrough,
    RunnableSequence,
)
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()


def word_count(text):
    return len(text.split())

prompt = PromptTemplate(
    template='Write a song about {topic}',
    input_variables=['topic']
)


song_gen_chain = RunnableSequence(prompt, model, parser)

parallel_chain = RunnableParallel(
    {
        'song': RunnablePassthrough(),
        'word_count': RunnableLambda(word_count)
    }
)

final_chain = RunnableSequence(song_gen_chain, parallel_chain)
result = final_chain.invoke({"topic": "love"})

print(result)

"""
{'song': "**Verse 1**\nIn the silence of a midnight 
sky\nI felt your presence passing by\nA whispered secret,
 a gentle breeze\nThat brought me to my knees\n\n
 **Chorus**\nOh, love, you're a fire that burns so bright\nA flame that flickers through the night\nYou're the safe haven whereI can hide\nThe place where my heart can reside\n\n**Verse 2**\nYour eyes, like sapphires, shining bright\nReflecting the beauty of our love's light\nYour touch, a whispered promise, a sweet caress\nThat sets my soul at rest\n\n**Chorus**\nOh, love, you're a fire that burns so bright\nA flame that flickers through the night\nYou're the safe haven where I can hide\nThe place where my heart can reside\n\n**Bridge**\nWe'll dance under starry skies\nWith every step, our love will rise\nWe'll laugh, we'll cry, we'll live and grow\nTogether, our love will forever glow\n\n**Chorus**\nOh, love, you're a fire that burns so bright\nA flame that flickers through the night\nYou're the safe haven where I can hide\nThe place where my heart can reside\n\n**Outro**\nIn your arms, I find my home\nWhere love resides, and I am never alone\nWith you, my heart beats as one\nIn this love, our forever has just begun.\n\nThis song is a ballad that explores the theme of love, with lyrics that describe the beauty, warmth, and comfort of being in a lovingrelationship. The song's melody is intended to be soaring and emotive, with a simple yet powerful rhythm that captures the 
intimacy and vulnerability of love.", 'word_count': 260}
"""