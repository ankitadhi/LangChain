from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

documents = [
    "Kathmandu is the capital of Nepal",
    "Paris is the capital of France",
    "This is not the time to panic"
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
    )

vector = embeddings.embed_query("What is the capital of Nepal?")    

vectors = embeddings.embed_documents(documents)
print(vector[:5])
print(f" {len(vectors)}, {len(vectors[0])}")

"""
Response:
[0.017528322, -0.0076990803, 0.01750906, -0.004669875, -0.005393041]
 3, 3072
"""
