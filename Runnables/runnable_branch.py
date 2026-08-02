from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableBranch,
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


prompt1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Summarize the following text \n {text}',
    input_variables=['text']
)

report_gen_chain = prompt1 | model | parser

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, prompt2 | model | parser),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

print(final_chain.invoke({'topic':'Russia vs Ukraine'}))


"""
The report provides an in-depth analysis of the ongoing conflict between Russia and Ukraine, which has its roots in the 19th century. The immediate cause of the conflict was the annexation of Crimea by Russia in 2014, following Ukraine's attempts to establish closer ties with the European Union. This led to international condemnation and sanctions.

Key events in the conflict include:

1. **Annexation of Crimea (2014):** Russia annexed Crimea, leading to international condemnation and sanctions.
2. **Minsk Agreements (2015):** Ukraine, Russia, and the European Union signed the Minsk Agreements, aiming to bring an end to the conflict.
3. **Separatist Takeover (2015):** Pro-Russian separatists took control of key cities in eastern Ukraine.
4. **Russian Military Intervention (2015):** Russia began providing military support to the separatists.
5. **Escalation of Hostilities (2022):** Russia launched a large-scale invasion of Ukraine, significantly escalating the conflict.

The conflict has resulted in a devastating humanitarian crisis, with thousands of people killed or injured and millions displaced. The international community has been divided in its response to the conflict, with the United States and the European Union imposing sanctions on Russia while other countries maintain diplomatic relations.

The report concludes that the conflict is complex and multifaceted, with deep historical and cultural roots. It recommends:

1. **Diplomatic Efforts:** Continued diplomatic efforts to resolve the conflict.
2. **Economic Sanctions:** Maintaining economic sanctions on Russia to pressure it to withdrawits troops from Ukraine.
3. **Humanitarian Aid:** Providing humanitarian aid to those affected by the conflict.
4. **Peacekeeping Efforts:** Deploying peacekeeping forces to the region to maintain stabilityand prevent further escalation.

Overall, the report emphasizes the need for a peaceful resolution to the conflict, which has had devastating consequences for the civilian population and the region as a whole.
"""