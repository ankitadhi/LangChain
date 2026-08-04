from langchain_text_splitters import (
    CharacterTextSplitter,
)

text = """
LangChain is an open-source framework.

It helps developers build applications powered by large language models.

Text splitters divide large documents into smaller chunks.

Character text splitters split the document based on characters.
"""

# Create a CharacterTextSplitter instance
splitter = CharacterTextSplitter(
    separator='\n',
    chunk_size=50,
    chunk_overlap=5
)





# Split the text into chunks
chunks = splitter.split_text(text)



# Print each
for chunk in chunks:
    print(f"Chunk: {chunk}\n")
    print(f"Chunk length: {len(chunk)}\n")
    print("-" * 40)   # Separator for better readability 


"""
Created a chunk of size 72, which is longer than the specified 50
Created a chunk of size 58, which is longer than the specified 50
Chunk: LangChain is an open-source framework.

Chunk length: 38

----------------------------------------
Chunk: It helps developers build applications powered by large language models.

Chunk length: 72

----------------------------------------
Chunk: Text splitters divide large documents into smaller chunks.

Chunk length: 58

----------------------------------------
Chunk: Character text splitters split the document based on characters.

Chunk length: 64

----------------------------------------

"""