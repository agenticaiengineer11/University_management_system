from dataclasses import dataclass
from enum import Enum
class Department(Enum):
    IT= "Information Technology"
    AI= "Artificial Intelligence"
    CS= "Computer Science"
    SE= "Software Engineering"

@dataclass
class Student:
    student_id: int
    name: str
    age: int
    department:Department
    cgpa: float
