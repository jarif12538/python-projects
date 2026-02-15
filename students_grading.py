student_grade = {}
def add_student_grade(name, grade):
    student_grade[name] = grade
    print(f"Adding grade for {name}: {grade}")
#update_student_grade("Alice", 85)  # This will print "Student Alice not found. Cannot update grade."
def update_student_grade(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"Updating grade for {name}: {grade}")
    else:
        print("**************************************")
        print(f"Student {name} not found. Cannot update grade.")
        print("**************************************")
def delete_student_grade(name):
    if name in student_grade:
        del student_grade[name]
        print(f"Deleted grade for {name}.")
    else:
        print("**************************************")
        print(f"Student {name} not found. Cannot delete grade.")
        print("**************************************")
def view_student_grade(name):
    if name in student_grade:
        print(f"{name}: {student_grade[name]}")
    else:
        print("**************************************")
        print(f"Student {name} not found. Cannot view grade.")
        print("**************************************")
def main():
    while True:
        print("\nStudent Grading System")
        print("1. Add Student Grade")
        print("2. Update Student Grade")
        print("3. Delete Student Grade")
        print("4. View Student Grade")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter student name: ")
            grade = int(input("Enter student grade: "))
            add_student_grade(name, grade)
        elif choice == '2':
            name = input("Enter student name: ")
            grade = int(input("Enter new student grade: "))
            update_student_grade(name, grade)
        elif choice == '3':
            name = input("Enter student name: ")
            delete_student_grade(name)
        elif choice == '4':
            name = input("Enter student name: ")
            view_student_grade(name)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
