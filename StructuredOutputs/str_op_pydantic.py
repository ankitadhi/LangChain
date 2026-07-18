from langchain_groq import ChatGroq
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import Literal, Optional

load_dotenv()

model = ChatGroq(
    model='qwen/qwen3-32b'
)

class Review(BaseModel):
    key_themes: list[str] = Field(description="Write down all the key themes discussed in the review in a list")
    summary: str = Field(description="A concise summary of the review, highlighting key points and overall impression.")
    sentiment: Literal['Positive', 'Negative', 'Neutral'] = Field(description="A concise sentiment.")
    pros: Optional[list[str]] = Field(description="Write down all the pros in a list")
    cons: Optional[list[str]] = Field(description="write down all the cos in a list.")
    name: Optional[str] = Field(description="Write the name of reviewer")


review_text = """I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by John Doe
"""

pydantic_model = model.with_structured_output(Review)

result = pydantic_model.invoke(review_text)

print(result)

"""
key_themes=['Performance and speed', 'Camera capabilities', 'Battery life and charging', 'Design ergonomics', 'Software ecosystem', 'Value proposition'] 
summary='The Samsung Galaxy S24 Ultra delivers exceptional performance with its Snapdragon 8 Gen 3 processor, stunning 200MP camerawith advanced zoom, and long-lasting battery life. However, its large size/weight, bloatware, and high price present notable drawbacks.' 
sentiment='Positive' 
pros=['Insanely powerful processor (great for gaming and productivity)', 'Stunning 200MP camera with incredible zoom capabilities', 'Long battery life with fast charging', 'S-Pen support is unique and useful'] 
cons=['Uncomfortable size/weight for one-handed use', 'Bloatware in One UI ecosystem', 'High price point ($1,300)'] 
name='John Doe'
"""