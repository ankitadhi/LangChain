from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

documents = [
    "Kathmandu is the capital of Nepal",
    "Paris is the capital of France",
    "This is not the time to panic", 
    "How are you today"
]

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview",
    dimensions=300
    )

doc_vectors = embeddings.embed_documents(documents)

query = "tell me about Kathmandu"

que_vector = embeddings.embed_query(query)

cosine_similarities = cosine_similarity([que_vector], doc_vectors)[0]
index, score = sorted(list(enumerate(cosine_similarities)),
             key=lambda x: x[1])[-1]   #reverse=True in decending 
print(f"Most similar document: {documents[index]} with score: {score}")

"""
Most similar document: Kathmandu is the capital of Nepal with score: 0.819113423374347""

"""
