from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

prompt1 = PromptTemplate(
    template='Generate a detailed report on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pionter summary about the \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'Langchain using Groq'})

print(result)

chain.get_graph().print_ascii()

"""
Here's a 5-point summary of the report on Langchain with Groq:

1. **Integration of Langchain and Groq**: Langchain, a conversational AI platform, has integrated with Groq, a company specializing in high-performance AI computing. This integration enables users to leverage Groq's high-performance computing capabilities to train and deploy conversational AI models at scale.

2. **Benefits of Langchain with Groq**: The integration provides several benefits, including improved performance, faster model training, and enhanced user experience. It also enables users to create custom conversational interfaces that provide a seamless and engaging user experience.

3. **Use Cases of Langchain with Groq**: The platform has several use cases, including virtual assistants, chatbots, and conversational interfaces for various applications such as customer service, sales, and marketing. It also enables developers to integrate with existing systems, such as CRM, ERP, and messaging platforms.

4. **Scalability and Performance**: Langchain with Groq provides scalability features to handle large volumes of conversations and user interactions, and enables developers to train and deploy AI models at scale using Groq's high-performance computing capabilities.

5. **Recommendation**: Based on the report, we recommend that developers and organizations consider Langchain with Groq for their conversational AI needs. The platform provides several benefits, including improved performance, faster model training, and enhanced user experience, making it an ideal platform for building custom conversational interfaces.
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +----------+         
      | ChatGroq |         
      +----------+         
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |  
+-----------------------+  
"""
