from langchain_text_splitters import HTMLHeaderTextSplitter

# The input HTML data
HTML_TEXT = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <style>
        body { font-family: sans-serif; margin: 40px; background: #f4f4f9; }
        .card { background: white; padding: 20px; border-radius: 8px; max-width: 300px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { margin-top: 0; color: #333; }
        ul { padding-left: 20px; }
    </style>
</head>
<body>

    <div class="card">
        <h1 id="name">John Doe</h1>
        <p><strong>Age:</strong> <span id="age">30</span></p>
        <p><strong>City:</strong> <span id="city">New York</span></p>
        <p><strong>Hobbies:</strong></p>
        <ul>
            <li>Reading</li>
            <li>Hiking</li>
        </ul>
    </div>

</body>
</html>
"""

headers = [
    ("h1", "header 1"),
    ("h2", "header 2"),
    ("h3", "header 3"),
]

# Initialize the splitter with the safe configuration
splitter = HTMLHeaderTextSplitter(
    headers_to_split_on=headers
)

# Execute the splitting process
chunks = splitter.split_text(HTML_TEXT)

# Print out results to confirm it works perfectly
for index, chunk in enumerate(chunks, 1):
    print(f"--- Chunk {index} ---")
    print(f"Content: {chunk.page_content.strip()}")
    print(f"Metadata: {chunk.metadata}")
    print("=" * 40)


"""
--- Chunk 1 ---
Content: John Doe
Metadata: {'header 1': 'John Doe'}
========================================
--- Chunk 2 ---
Content: Age:  
30  
City:  
New York  
Hobbies:  
Reading  
Hiking
Metadata: {'header 1': 'John Doe'}
========================================
"""