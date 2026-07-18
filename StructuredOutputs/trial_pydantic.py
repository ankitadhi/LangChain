from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):

    name: str = "Ankit"
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0.0, lt=10.0, default=5.0, description="Decimal value representing the cgpa of students")

new_student = {'age': '20' ,'email': 'abc@abc.gmail.com', 'cgpa': 7.5}
student = Student(**new_student)

print(student)
