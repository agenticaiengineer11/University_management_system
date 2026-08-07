from app.models import Student
from app.services import add_student

student = Student(
    student_id=2,
    name="Ali",
    age=21,
    department="Computer Science",
    cgpa=3.60
)

result = add_student(student)

print(result)