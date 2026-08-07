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

    