from typing import TypedDict


class State(TypedDict):
    message: list
    user_name: str
    count: int


def process(state: State):
    state['count'] +=1
    state['answer'] = "Processed : " + state['question']
    return state


state = {
    'question': 'What is RAG?',
    'answer': "",
    'count': 0
}


state = process(state)

print(state)