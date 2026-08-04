from langchain_text_splitters import (
    TokenTextSplitter,
)

text = """
LangChain is an open-source framework.

It helps developers build applications powered by large language models.

Text splitters divide large documents into smaller chunks.

Character text splitters split the document based on characters.
"""


#Using Token Text Splitter
splitter = TokenTextSplitter(
    chunk_size=20,
    chunk_overlap=10
)


#split the text into chunks
chunks = splitter.split_text(text)

#Print the chunks
for chunk in chunks:
    print(f"Token Chunk: {chunk}\n")
    print(f"Token Chunk length: {len(chunk)}\n")
    print("=" * 40)   # Separator for better readability


"""
Token Chunk: 
LangChain is an open-source framework.

It helps developers build applications powered by

Token Chunk length: 90

========================================
Token Chunk: .

It helps developers build applications powered by large language models.

Text splitters divide

Token Chunk length: 98

========================================
Token Chunk:  large language models.

Text splitters divide large documents into smaller chunks.

Character text

Token Chunk length: 99

========================================
Token Chunk:  large documents into smaller chunks.

Character text splitters split the document based on characters.


Token Chunk length: 104

========================================
"""