from langchain_core.tools import BaseTool
from pydantic import BaseModel, Field


#Define theinput schema for the tool
class CalculatorInput(BaseModel):
    a: int = Field(description='First Number')
    b: int = Field(description='Second Number')


#Create the custom tool
class AddTool(BaseTool):

    name: str = 'add_numbers'

    description: str = 'Add two numbers together'

    args_schema: type[BaseModel] = CalculatorInput

    def _run(self, a: int, b: int) -> int:
        return a+b

#Create an instance of tool
add_tool = AddTool()


#Call the tool
result = add_tool.invoke({
    'a': 10,
    'b': 30
})

print(result)
