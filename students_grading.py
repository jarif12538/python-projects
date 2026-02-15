student_grade = {}
def add_student_grade(name, grade):

    student_grade[name] = grade
    print(f"Adding grade for {name}: {grade}")
def update_student_grade(name, grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"Updating grade for {name}: {grade}")
        
    else:
        print(f"Student {name} not found. Cannot update grade.")
def get_student_grade(name):
    grade = student_grade.get(name)
    if grade is not None:
        print(f"Grade for {name}: {grade}")
        return grade
    else:
        print(f"Student {name} not found. No grade available.")
        return None
def calculate_average_grade():    
    if student_grade:
        average = sum(student_grade.values()) / len(student_grade)
        print(f"Average grade: {average:.2f}")
    
    else:        
        print("No grades available to calculate average.")
        