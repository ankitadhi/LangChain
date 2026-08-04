from langchain_community.document_loaders import BSHTMLLoader

loader = BSHTMLLoader(
    file_path="page.html",
    bs_kwargs={"features": "html.parser"}
)

documents = loader.load()

for idx, doc in enumerate(documents):
    print(f"--- Document {idx + 1} ---")
    print("PAGE CONTENT:")
    print(doc.page_content)
    print("\nMETADATA:")
    print(doc.metadata)
    print("-" * 20)


"""
PAGE CONTENT:





User Profile




John Doe
Age: 30
City: New York
Hobbies:

Reading
Hiking






METADATA:
{'source': 'page.html', 'title': 'User Profile'}
--------------------
(env) 
"""