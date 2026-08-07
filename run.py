from app.models import Student
from app.services import add_student,search_student, update_student,delete_student

student = Student(
    student_id=2,
    name="Ali",
    age=21,
    department="Computer Science",
    cgpa=3.60
)

result = add_student(student)

print(result)
data = search_student(1)
print(data)

updated_student = Student(
    student_id=2,
    name="Mukurram Aziz",
    age=23,
    cgpa=3.75,
    department="Information Technology"
)

d = update_student(updated_student)
print(d)

f = delete_student(2)
print(f)