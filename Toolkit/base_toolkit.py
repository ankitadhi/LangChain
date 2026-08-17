from dotenv import load_dotenv

from langchain_core.tools import BaseTool, BaseToolkit, tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()


# ============================================================
# LLM
# ============================================================

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash"
)


# ============================================================
# CUSTOM TOOLS
# ============================================================

@tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@tool
def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


@tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@tool
def divide(a: float, b: float) -> float:
    """Divide a by b."""

    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


# ============================================================
# CUSTOM TOOLKIT
# ============================================================

class CalculatorToolkit(BaseToolkit):

    def get_tools(self) -> list[BaseTool]:
        """Return all calculator tools."""

        return [
            add,
            subtract,
            multiply,
            divide
        ]


# ============================================================
# CREATE TOOLKIT
# ============================================================

toolkit = CalculatorToolkit()

tools = toolkit.get_tools()


# Display available tools
print("Available tools:")

for tool in tools:
    print(f"- {tool.name}")


# ============================================================
# BIND TOOLS TO LLM
# ============================================================

llm_with_tools = llm.bind_tools(tools)


# ============================================================
# ASK THE LLM
# ============================================================

response = llm_with_tools.invoke(
    "Calculate 20 multiplied by 5"
)


# ============================================================
# DISPLAY LLM RESPONSE
# ============================================================

print("\nLLM Response:")
print(response)

print("\nTool Calls:")
print(response.tool_calls)


# ============================================================
# EXECUTE TOOL CALLS
# ============================================================

tool_map = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}


for tool_call in response.tool_calls:

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]

    selected_tool = tool_map.get(tool_name)

    if selected_tool is None:
        print(f"Unknown tool: {tool_name}")
        continue

    result = selected_tool.invoke(tool_args)

    print("\nTool Executed:")
    print(f"Tool: {tool_name}")
    print(f"Arguments: {tool_args}")
    print(f"Result: {result}")