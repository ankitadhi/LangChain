from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableSequence
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.7
)

parser = StrOutputParser()


prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)


parallel_chain=RunnableParallel(
    {
        "tweet": RunnableSequence(prompt1, model, parser),
        "linkedin_post": RunnableSequence(prompt2, model, parser)
    }
)

result = parallel_chain.invoke({"topic": "AI in Healthcare"})
print(result)

"""
{'tweet': '"Revolutionizing patient care, one diagnosis 
at a time. Artificial Intelligence in healthcare is 
transforming the way doctors diagnose diseases, develop 
personalized treatment plans, and enhance patient outcomes. 
The future of medicine is here! #AIinHealthcare 
#DigitalHealth"', # 
 'linkedin_post': "**Revolutionizing Healthcare with AI: 
 The Future is Now**\n\nAs we continue to navigate the 
 ever-evolving landscape of healthcare, one thing is 
 clear: Artificial Intelligence (AI) is poised to 
 revolutionize the way we diagnose, treat, and deliver 
 care. From predictive analytics to personalized medicine, 
 AI is empowering healthcare professionals to make more 
 informed decisions, improve patient outcomes, and 
 enhance the overall care experience.\n\n**The Impact of AI on Healthcare**\n\n1. **Early Disease Detection**: AI-powered tools can analyze medical images, lab results, and patient data to identify potential health risks and detect diseases at an early stage.\n2. **Personalized Medicine**: AI-driven analytics can help tailor treatment plans to individual patients, taking into account their unique genetic profiles, medical histories, and lifestyle factors.\n3. **Streamlined Clinical Workflows**: AI can automate routine tasks, freeing up healthcare professionals to focus on high-value tasks that require human expertise and compassion.\n4. **Improved Patient Engagement**: AI-powered chatbots and virtual assistants can help patients navigate the healthcare system, answer questions, and provide support 24/7.\n\n**The Future of Healthcare**\n\nAs AI continues to advance, we can expect to see even more innovative applications in healthcare, including:\n\n1. **Telemedicine**: AI-powered platforms can connect patients with healthcare professionals remotely, expanding access to care and improving health outcomes.\n2. **Genomic Medicine**: AI can help analyze vast amounts ofgenomic data, leading to new insights into disease mechanisms and personalized treatment options.\n3. **Population Health Management**: AI can help healthcare organizations identify high-risk patient populations and develop targeted interventions to improve health outcomes.\n\n**Jointhe Conversation**\n\nAs we continue to explore the potential of AI in healthcare, I'd love tohear from you:\n\n* What are your thoughts on the role of AI in healthcare?\n* How do you see AI impacting your work or the healthcare industry as a whole?\n* What innovations do you think are most promising in the field of AI and healthcare?\n\nLet's work together to create a futurewhere AI enhances, rather than replaces, human compassion and expertise in healthcare.\n\n**#AIinHealthcare #HealthcareInnovation #FutureOfHealthcare**\n\n(Note: You can customize this postto fit your personal style and industry expertise. 
Feel free to add or remove sections as needed.)"}
"""