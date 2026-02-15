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
        print(f"Student {name} not found. Cannot update grade.")
def delete_student_grade(name):
    if name in student_grade:
        del student_grade[name]
        print(f"Deleted grade for {name}.")
    else:
        print(f"Student {name} not found. Cannot delete grade.")
def view_student_grade(name):
    if name in student_grade:
        for student, grade in student_grade.items():
            print(f"{student}: {grade}")
    else:
        print(f"Student {name} not found. Cannot view grade.")