import random

class DupliLLM:
    def __init__(self):
        print('LLM created')

    def predict(self, prompt):

        response_list=[
            'Delhi is the capital of India.',
            'IPL is a cricket league.',
            'AI stands for Artificial Intelligence.'
        ]
        print('predicting')
        return{ 'response': random.choice(response_list)}

llm = DupliLLM()

print(llm.predict('What is the capital of India'))


# Prompt Template Example

class DupliPromptTemplate():

    def __init__(self, template, input_variables):
        self.template = template
        self.input_variables = input_variables

    def format(self, input_dict):
        return self.template.format(**input_dict)


template = DupliPromptTemplate(
    template='Write a poem about {topic} ',
    input_variables=['topic']
)

prompt = template.format({'topic': 'love'})
print(prompt)

#prediction using prompt template

result = llm.predict(prompt)
print(result)

class DupliLLMChain():
    def __init__(self, llm, prompt):
        self.llm = llm
        self.prompt = prompt

    def run(self, input_dict):

        final_prompt = self.prompt.format(input_dict)
        result = self.llm.predict(final_prompt)
        return result['response']


template1 = DupliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

chain = DupliLLMChain(llm, template1)


respond = chain.run({'length': 'short', 'topic': 'Nepal'})

print(respond)


"""
LLM created
predicting
{'response': 'AI stands for Artificial Intelligence.'}
Write a poem about love 
predicting
{'response': 'IPL is a cricket league.'}
predicting
IPL is a cricket league.
(env) """
