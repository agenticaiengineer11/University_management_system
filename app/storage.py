import json
from pathlib import Path
from app.models import Student

DATA_FILE = Path(__file__).parent.parent / "data" / "students.json"

def load_students()-> list:
    try:
        with open(DATA_FILE,"r") as file:
            students = json.load(file)
        return students
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_students(students:list) ->None:
    try:
        with open(DATA_FILE,"w") as file:
            json.dump(students,file, indent=4)
    except Exception as e:
        print(f"Error saving students: {e}")

students = [
    {
        "student_id": 1,
        "name": "Noman",
        "age": 22,
        "department": "Software Engineering",
        "cgpa": 3.75
    }
]

save_students(students)
    