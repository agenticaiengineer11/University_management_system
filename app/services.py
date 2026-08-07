from app.models import Student
from dataclasses import asdict
from app.validators import (
    validate_name,
    validate_age,
    validate_cgpa,
    validate_student_id
)
from app.storage import load_students , save_students

def add_student(student: Student) -> bool:

    if not validate_student_id(student.student_id):
        print("Student ID validation failed")
        return False

    if not validate_name(student.name):
        print("Name validation failed")
        return False

    if not validate_age(student.age):
        print("Age validation failed")
        return False

    if not validate_cgpa(student.cgpa):
        print("CGPA validation failed")
        return False

    students = load_students()

    for existing_student in students:
        if existing_student["student_id"] == student.student_id:
            print("Duplicate Student ID")
            return False

    student_dict = asdict(student)
    students.append(student_dict)
    save_students(students)

    print("Student added successfully")
    return True