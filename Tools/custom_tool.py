from langchain_core.tools import tool


#Step 1 create a function

def multiply(a, b):
    """Multiply two numbers"""
    return a*b

#Step 2 add type hints
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b


#Step 3 add a tool decorator

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a*b


result = multiply.invoke({'a': 3, 'b': 5})

print(result)
print(multiply.name)
print(multiply.description)
print(multiply.args_schema)


"""
15
multiply
Multiply two numbers
<class 'langchain_core.utils.pydantic.multiply'>
"""