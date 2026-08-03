from langchain_community.document_loaders import JSONLoader

loader = JSONLoader(
    file_path='./smaple.json',
    jq_schema='.[] ', 
    text_content=False,
    )  #for extracting only specific content from json file for ex hobbies only use jq_schemas='.hobbies[]

documents = loader.load()

for doc in documents:
    print(doc.page_content)

