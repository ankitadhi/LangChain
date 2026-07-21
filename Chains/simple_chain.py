from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}", 
    input_variables=['topic']    
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'langurburja game played in Nepal'})

print(result)


"""I've found some limited information on the Langur Burja game played in Nepal. Here are 5 interesting facts:

1. **Traditional Game**: Langur Burja is a traditional game played in the Himalayas of Nepal. It's a popular folk game among the indigenous communities of the region.

2. **Objective**: The objective of the game is to score points by throwing a stone or a small piece of wood at the target, which is usually marked on a stone or a wooden pole. The player who scores the most points wins.

3. **Involves Agility and Accuracy**: Langur Burja requires a combination of agility and accuracy. Players need to run towards the target and throw the stone or piece of wood with precisionto score points. The game also involves physical exercise, making it a fun and engaging activity for participants.

4. **Played during Festivals**: Langur Burja is often played during festivals and celebrationsin Nepal, particularly during the Dashain festival. The game is a way to bring people togetherand create a sense of community.

5. **Rich Cultural Significance**: Langur Burja has a rich cultural significance in Nepal, particularly among the indigenous communities. The game is a way to preserve traditional practicesand pass them down to future generations. It also serves as a way to showcase the community's skills and abilities.

Please note that information on Langur Burja game is limited, and it's not widely known. Thesefacts are based on my research, and I'm not an expert in Nepalese culture or traditions.

"""

chain.get_graph().print_ascii()