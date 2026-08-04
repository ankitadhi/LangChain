from langchain_community.document_loaders import CSVLoader


loader = CSVLoader(file_path ='./Social_Network_Ads.csv')

documents = loader.load()

print(documents[0].page_content)

"""
User ID: 15624510
Gender: Male
Age: 19
EstimatedSalary: 19000
Purchased: 0
"""
