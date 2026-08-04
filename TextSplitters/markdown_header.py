from langchain_text_splitters import MarkdownHeaderTextSplitter

MARKDOWN_TEXT = """
# Introduction

LangChain...

## Installation

pip install...

## Examples

Example code...
"""

# Using Markdown Header Text Splitter
header = [
    ('#', 'Header 1'),
    ('##', 'Header 2'),
]


splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=header
)

chunks = splitter.split_text(MARKDOWN_TEXT)

for chunk in chunks:
    print(f"Markdown Header Content: {chunk.page_content}\n")
    print(f"Markdown Header Metadata: {chunk.metadata}\n")
    print("=" * 40)   # Separator for better readability


"""
Markdown Header Content: pip install...

Markdown Header Metadata: {'Header 1': 'Introduction', 'Header 2': 'Installation'}

========================================
Markdown Header Content: Example code...

Markdown Header Metadata: {'Header 1': 'Introduction', 'Header 2': 'Examples'}

========================================
"""