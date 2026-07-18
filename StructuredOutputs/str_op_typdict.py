#generating Structured Outputs from Models
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal


load_dotenv()

class Person(TypedDict):
    name: str
    age: int
    email: str

new_person: Person = {
    "name": "John Doe",
    'age': 25,
    "email": 'john.doe@example.com'
    }

#Reviews -> LLm ->{summary:"", sentiment: ""}


review = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Nitish Singh
"""

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
)


#Schema
class Review(TypedDict):
    summary: str
    sentiment: str

class AnnotatedReview(TypedDict):
    summary: Annotated[str, "A concise summary of the review, highlighting key points and overall impression."]
    sentiment: Annotated[str, "A concise sentiment with probability"]

class ReviewWithDetails(TypedDict):
    key_themes: Annotated[list[str], 
                        "Write down all the key themes discussed in the review in a list"]
    summary: Annotated[str,
                       "A concise summary of the review, highlighting key points and overall impression."]
    sentiment: Annotated[str, 
                        "A concise sentiment with confidence value"]
    pros: Annotated[Optional[list[str]],
                        "Write down all the pros in a list"]
    cons: Annotated[Optional[list[str]],
                    "Write down all the cons in a list"]
    name: Annotated[Optional[str], 
                    "Write the name of the reviewer"]


# structured_model = model.with_structured_output(Review)

# result = structured_model.invoke(review)

# print(result)

# annotated_structured_model = model.with_structured_output(AnnotatedReview)
detailed_model = model.with_structured_output(ReviewWithDetails)
result = detailed_model.invoke(review)


for key, value in result.items():
    print(f"{key}: {value}")

"""
cons: ['Weight and size make it uncomfortable for one-handed use', 'Samsung’s One UI comes with bloatware (e.g., multiple Samsung apps for Google services)', 'High price tag of $1,300', '200MP camera loses quality when zooming beyond 30x']
key_themes: ['High-performance hardware (Snapdragon 8 Gen 3)', 'Camera capabilities (200MP, night mode, zoom)', 'Battery life and fast charging', 'S-Pen integration', 'User interface (One UI) bloatware', 'Device pricing']
name: Nitish Singh
pros: ['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful']
sentiment: Positive (85% confidence) - Enthusiastic about performance and camera but critical of design, bloatware, and pricing
summary: The Samsung Galaxy S24 Ultra is a powerhouse with a top-tier processor, 200MP camera,and long 5000mAh battery. The S-Pen adds unique value, but the phone's weight, bloatware, and $1,300 price tag may deter buyers. Overall, it excels in performance and imaging but compromises on portability and user experience.
"""