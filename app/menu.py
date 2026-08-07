from app.models import Student
from app.services import (
    add_student,
    search_student,
    update_student,
    delete_student
)

def show_menu() -> None:

    print("\n" + "=" * 50)
    print("     UNIVERSITY MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

def main()->None:
    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            print("\n ===============Add New Student=============")
            student_id = int(input("Enter Student ID: "))
            name = input("Enter Student Name: ").strip()
            age = int(input("Enter Student Age: "))
            department = input("Enter Department: ").strip()
            cgpa = float(input("Enter CGPA: "))

            student = Student(
            student_id=student_id,
            name=name,
            age=age,
            department=department,
            cgpa=cgpa
)
            result = add_student(student)
            if result:
                print("\n✅ Student added successfully.")
            else:
                print("\n❌ Failed to add student.")
if __name__ == "__main__":
    main()