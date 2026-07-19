from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = JsonOutputParser()


template = PromptTemplate(
    template='Give me the name, age and city of a fictional person in Greek Mythology. \n{format_instruction}',
    input_variables=[], 
    partial_variables={
        'format_instruction': parser.get_format_instructions()
    }
)

prompt = template.format()

# print(prompt)

response = model.invoke(prompt)

# print(response)

final_result = parser.parse(response.content)
# print(final_result)


"""Response:
{'name': 'Khaoson', 'age': 250, 'city': 'Elyria'}
"""

#Json Parser Using Chains

template1 = PromptTemplate(
    template='Give me 5 amazing facts about {country} that someone outside of it would not understand . \n{{format_instruction}}',
    input_variables=['country'],
    partial_variables={'format_instructions': parser.get_format_instructions()} 
)

chain = template1 | model | parser
response = chain.invoke({'country': 'Nepal'})

print(response) 


"""Response

1. **The concept of "Tapu"**: In Nepal, especially in rural areas, a "Tapu" is a sacred boundary or a demarcation line that marks the territory of a family, a community, or a village. People in Nepal believe that crossing the Tapu can bring bad luck, misfortune, or even death. This concept is deeply rooted in their culture and is often respected by locals.

2. **The significance of "Mithi"**: In Nepalese culture, a "Mithi" is a type of sacred bond or a promise that is made to someone, usually between two people who are not related by blood. This promise is often made during festivals, weddings, or other significant events, and it is considered a sacred vow that must be honored. Breaking a Mithi can lead to severe consequences, including social ostracism and even family feuds.

3. **The importance of "Kumari" in Nepalese culture**: In Nepal, a "Kumari" is a young girl who is believed to be the incarnation of the goddess Durga. She is chosen for this role from a young age and is considered sacred. The Kumari is responsible for performing rituals and ceremonies, and is often sought out for blessings and guidance. However, the Kumari's life is also marked by strict rules and rituals, including the fact that she is not allowed to leave her home or interact with men outside of her family.

4. **The concept of "Hijra" in Nepal**: In Nepal, a "Hijra" is a type of third-gender individual who is considered neither male nor female. Hijras are often revered for their spiritual powers and are sought out for blessings and guidance. However, they also face significant social stigma and discrimination, and are often forced to live on the margins of society.

5. **The significance of "Ghumsi" in Nepalese culture**: In Nepal, a "Ghumsi" is a type of ritual where a family or community comes together to perform a sacred ceremony to ward off evil spirits and bring good luck. During this ceremony, the participants engage in various rituals, including singing, dancing, and offering prayers to the gods. The Ghumsi is often performed during times of crisis or transition, such as during weddings, funerals, or when a family member is ill.

These are just a few examples of the many fascinating customs and traditions that exist in Nepal. Each of these facts offers a glimpse into the rich cultural heritage of this beautiful country.
"""