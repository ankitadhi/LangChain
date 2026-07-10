#use the open source model locally

from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen-2.5-7B-Instruct",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 512,
        "temperature": 0.7
        }
    )

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital city of Nepal?")

print(response.content)
