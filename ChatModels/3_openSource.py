# Using open source models from hugging face rather than paid models
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

load_dotenv()

# Creating a model
llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",  # or Qwen2.5-72B-Instruct, etc.
    task="text-generation",
    max_new_tokens=512
)

# FIX: Changed 'model=llm' to 'llm=llm'
model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital city of Nepal?")

print(result.content)

"""
Response:
The capital city of Nepal is Kathmandu.
"""

