from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage  
from langchain_core.messages import ChatMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(
    model="qwen/qwen3-32b",
    temperature=1.0,
    )

chat_template = ChatPromptTemplate([
    ('system', "You are a helpful abd intelligent {domain} expert"),
    ('human', "Explain in simple terms about the {topic}")
])

prompt = chat_template.invoke({
    "domain": "AI",
    "topic": "machine learning"
})

response = model.invoke(prompt)

print(response.content)


"""
**Machine Learning Explained Simply**  

Think of **machine learning** like teaching a robot (or software) to learn from experience, just as humans do—**without being told every single rule**. Instead of programming it step-by-step, we give it lots of examples, and it figures out patterns on its own to make decisions or predictions.  

---

### **How Does It Work?**  
1. **Data is the Teacher**:  
   - You feed the system a ton of examples.  
   - Example: If you want to teach a model to tell dogs from cats, show it thousands ofpictures labeled "dog" or "cat."  

2. **It Learns Patterns**:  
   - The system looks for hidden patterns in the data.  
   - Example: It might notice that round ears and pointy noses often mean "cat."  

3. **Practice Makes Perfect**:  
   - The model becomes better at guessing new examples.  
   - Example: After training, if you show it a new animal photo, it tries to say "cat" or "dog."  

---

### **Types of Machine Learning**  
- **Supervised Learning**:  
  - **Labeled Examples**: The model learns from answers (like labeled cat/dog photos).  
  - Example: Predicting house prices based on past prices.  

- **Unsupervised Learning**:  
  - **No Labeled Answers**: The model finds hidden patterns on its own.  
  - Example: Grouping similar songs together for a playlist.  

- **Reinforcement Learning**:  
  - **Trial & Error**: The model learns by trying things and getting rewards for good choices.  
  - Example: Training a robot to walk by giving points for each step it takes.  

---

### **Real-World Use**  
- **Spam Filters**: Learn what spam looks like by analyzing old emails.  
- **Netflix Recommendations**: Suggests shows you’ll like based on what others (or you)watched.  
- **Medical Diagnosis**: Helps doctors find cancers in X-rays by spotting unusual patterns.  

---

### **Key Idea**  
Machine learning is like teaching a child through examples—**the more examples (data), the smarter it gets**. It doesn’t know the rules upfront; it discovers them through practice. The more it tries, the better it becomes! 🤖📚  

*(Simple enough for cookies, right?)* 🍪
"""