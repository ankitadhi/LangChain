from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_chroma import Chroma
load_dotenv()


embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2-preview"
    )

#Create a langchain document for  ipl players

doc1 = Document(
        page_content="Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.",
        metadata={"team": "Royal Challengers Bangalore"}
    )
doc2 = Document(
        page_content="Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.",
        metadata={"team": "Mumbai Indians"}
    )
doc3 = Document(
        page_content="MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.",
        metadata={"team": "Chennai Super Kings"}
    )
doc4 = Document(
        page_content="Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.",
        metadata={"team": "Mumbai Indians"}
    )
doc5 = Document(
        page_content="Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.",
        metadata={"team": "Chennai Super Kings"}
    )


docs = [doc1, doc2, doc3, doc4, doc5]

#Create a Chroma vector store from the documents and embeddings
vector_store = Chroma.from_documents(
    documents=docs,
    persist_directory="./IPL_chromadb",
    embedding=embeddings,
)


#Add the documents to the vector store
# vector_store.add_documents(docs)


# result = vector_store.get(include=['embeddings', 'documents', 'metadatas'])

# print(result)

# search documents
# results = vector_store.similarity_search(
#     query='Who among these are a bowler?',
#     k=2
# )

#search similarity with scores
results_with_scores = vector_store.similarity_search_with_score(
    query='Who among these are a bowler?',
    k=2
)

for result, score in results_with_scores:
    print(f"Content: {result.page_content}, Score: {score}")

"""
Content: Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise., Score: 0.6193535327911377
Content: Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise., Score: 0.6193535327911377
{'ids': ['70fc72d9-76bf-49c5-ab07-1812a00b284a', 'ba4ab941-dc6b-4276-889a-d01c35b4ceb2', 'e3f9f5f5-8d6b-4c8b-b8b1-59a3dc192a0c', '0a659856-2017-4f63-9845-20686e597522', '4a2aba6a-6dd2-4d83-b370-7da6b6915f04'], 'embeddings': array([[ 0.0074764 ,  0.01034819,  0.01265225, ...,  0.00313006,
         0.01334844,  0.00201392],
       [ 0.00578349,  0.03275334, -0.00712996, ...,  0.00599   ,
         0.00842474,  0.01284763],
       [ 0.00278233,  0.02150997, -0.00733589, ..., -0.00771123,
         0.01547233,  0.01310577],
       [ 0.03408059,  0.01119854, -0.01184934, ...,  0.00848975,
         0.02335239, -0.0077354 ],
       [-0.00296271,  0.01466555, -0.01345706, ...,  0.00715038,
         0.01247527,  0.00910379]], shape=(5, 3072)), 'documents': ['Virat Kohli is one of the most successful and consistent batsmen in IPL history. Known for his aggressive batting style and fitness, he has led the Royal Challengers Bangalore in multiple seasons.', "Rohit Sharma is the most successful captain in IPL history, leading Mumbai Indians to five titles. He's known for his calm demeanor and ability to play big innings under pressure.", 'MS Dhoni, famously known as Captain Cool, has led Chennai Super Kings to multiple IPL titles. His finishing skills, wicketkeeping, and leadership are legendary.', 'Jasprit Bumrah is considered one of the best fast bowlers in T20 cricket. Playing for Mumbai Indians, he is known for his yorkers and death-over expertise.', 'Ravindra Jadeja is a dynamic all-rounder who contributes with both bat and ball. Representing Chennai Super Kings, his quick fielding and match-winning performances make him a key player.'], 'uris': None, 'included': ['embeddings', 'documents', 'metadatas'], 'data': None, 'metadatas': [{'team': 'Royal Challengers Bangalore'}, {'team': 'Mumbai Indians'}, {'team': 'Chennai Super Kings'}, {'team': 'Mumbai Indians'}, {'team': 'Chennai Super Kings'}]}
"""