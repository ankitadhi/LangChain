from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)


# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | template2 | model | parser

result = chain.invoke({'topic': 'Samsung galaxy S26 Ultra'})

print(result)

"""
Here is a 5-line summary of the Samsung Galaxy S26 Ultra report:

The Samsung Galaxy S26 Ultra features a 6.8-inch Dynamic 
AMOLED display with a 120Hz refresh rate, providing an 
immersive viewing experience. The phone's quad-camera setup
includes a 50MP primary sensor, 12MP telephoto lens, 12MP 
periscope lens, and 108MP ultra-wide lens, capable of 
recording 8K video. The Galaxy S26 Ultra is powered by a
5000mAh battery, Qualcomm Snapdragon 8Gen 2 chipset, and supports
fast charging, wireless charging, and reverse wireless 
charging. It also features a range of additional features, 
including an S-Pen, DeX, and IP67 water and dust resistance. 
The phone runs on Android 13 with Samsung's One UI 5.1 skin, 
offering a seamless software experience.
"""