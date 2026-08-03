from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('../LangChain_Learning_Journey_Notes.pdf')

documents = loader.load()

print(documents[0].metadata)


"""
{'producer': 'Qt 5.15.13', 
'creator': 'wkhtmltopdf 0.12.6', 
'creationdate': '2026-07-18T04:39:43+00:00', 
'title': '', 'source': '../LangChain_Learning_Journey_Notes.pdf', '
total_pages': 12, 'page': 0, 'page_label': '1'}
"""