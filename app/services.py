import logging
logger = logging.getLogger(__name__)
from app.models import Student
from dataclasses import asdict
from app.exceptions import StudentNotFoundError,ValidationError,DuplicateStudentError
from app.validators import (
    validate_name,
    validate_age,
    validate_cgpa,
    validate_student_id
)
from app.storage import load_students , save_students

def add_student(student: Student) -> bool:
    logger.info("add_student() called")

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
            raise DuplicateStudentError(
                f"Student ID {student.student_id} already exists."
        )

    student_dict = asdict(student)
    students.append(student_dict)
    save_students(students)
    logger.info(
    f"Student added successfully | ID: {student.student_id} | Name: {student.name}"
)
    return True

def search_student(student_id: int):
    if not validate_student_id(student_id):
        raise ValidationError("Invalid student ID.")

    students = load_students()

    for student in students:
        if student["student_id"] == student_id:
            return student

    raise StudentNotFoundError(
        f"Student with ID {student_id} was not found."
    )

def update_student(updated_student:Student) ->bool:
    if not validate_student_id(student.student_id):
        raise ValidationError("Invalid student ID.")

    if not validate_name(student.name):
        raise ValidationError("Invalid student name.")

    if not validate_age(student.age):
        raise ValidationError("Invalid student age.")

    if not validate_cgpa(student.cgpa):
        raise ValidationError("Invalid CGPA.")
    students = load_students()

    for index , student in enumerate(students):
        if student["student_id"] == updated_student.student_id:
            students[index] = asdict(updated_student)
            save_students(students)
            return True

    raise StudentNotFoundError(
    f"Student with ID {student.student_id} was not found."
)
def delete_student(student_id: int) -> bool:

    if not validate_student_id(student.student_id):
        raise ValidationError("Invalid student ID.")

    students = load_students()

    for index, student in enumerate(students):

        if student["student_id"] == student_id:

            students.pop(index)

            save_students(students)

            return True

    raise StudentNotFoundError(
    f"Student with ID {student_id} was not found."
)
def get_all_students():
    return load_students()