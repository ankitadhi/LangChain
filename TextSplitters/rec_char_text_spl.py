from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
)

text = """
LangChain is an open-source framework.

It helps developers build applications powered by large language models.

Text splitters divide large documents into smaller chunks.

Character text splitters split the document based on characters.
"""


#Using Recursive Character Splitter
char_splitter = RecursiveCharacterTextSplitter(
    separators=["\n", '. ', ' ', ''],  # Note the plural 'separators'
    chunk_size=50,
    chunk_overlap=5
)


#split the text into chunks
rec_chunks = char_splitter.split_text(text)


# Recursive Character Splitter Example
for chunk in rec_chunks:
    print(f"Recursive Chunk: {chunk}\n")
    print(f"Recursive Chunk length: {len(chunk)}\n")
    print("=" * 40)   # Separator for better readability


"""
Recursive Chunk: LangChain is an open-source framework.

Recursive Chunk length: 38

========================================
Recursive Chunk: It helps developers build applications powered by

Recursive Chunk length: 49

========================================
Recursive Chunk: by large language models.

Recursive Chunk length: 25

========================================
Recursive Chunk: Text splitters divide large documents into

Recursive Chunk length: 42

========================================
Recursive Chunk: into smaller chunks.

Recursive Chunk length: 20

========================================
Recursive Chunk: Character text splitters split the document based

Recursive Chunk length: 49

========================================
Recursive Chunk: on characters.

Recursive Chunk length: 14

========================================
"""