from app.models import Student
from app.exceptions import StudentNotFoundError, ValidationError
from app.services import (
    add_student,
    search_student,
    update_student,
    delete_student,
    get_all_students
)

def get_integer_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_float_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")
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
        elif choice == "2":
            print("\n========== Search Student ==========")

            student_id = int(input("Enter Student ID: "))

            try:
                student = search_student(student_id)

                print("\nStudent Found")
                print(f"Student ID : {student['student_id']}")
                print(f"Name       : {student['name']}")
                print(f"Age        : {student['age']}")
                print(f"Department : {student['department']}")
                print(f"CGPA       : {student['cgpa']}")

            except StudentNotFoundError as error:
                print(f"\n❌ {error}")

            except ValidationError as error:
                print(f"\n❌ {error}")
        
        elif choice == "3":
            print("\n========== Update Student ==========")

            student_id = get_integer_input("Enter Student ID: ")
            name = input("Enter Updated Name: ").strip()
            age = get_integer_input("Enter Updated Age: ")
            department = input("Enter Updated Department: ").strip()
            cgpa = get_float_input("Enter Updated CGPA: ")

            updated_student = Student(
                student_id=student_id,
                name=name,
                age=age,
                department=department,
                cgpa=cgpa
            )

            result = update_student(updated_student)

            if result:
                print("\n✅ Student updated successfully.")
            else:
                print("\n❌ Student not found or invalid data.")
        elif choice == "4":
            print("\n========== Delete Student ==========")
            student_id = int(input("Enter Student ID: "))
            result = delete_student(student_id)
            if result:
                print("\n✅ Student deleted successfully.")
            else:
                print("\n❌ Student not found.")
        elif choice == "5":
            print("\n========== All Students ==========")

            students = get_all_students()

            if not students:
                print("No students found.")
            else:
                for student in students:
                    print("-" * 40)
                    print(f"Student ID : {student['student_id']}")
                    print(f"Name       : {student['name']}")
                    print(f"Age        : {student['age']}")
                    print(f"Department : {student['department']}")
                    print(f"CGPA       : {student['cgpa']}")
        elif choice == "6":
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Please try again.")
if __name__ == "__main__":
    main()