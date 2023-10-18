# Initialize a list to store student data
student_data = []

while True:
    name = input("Enter the student's name (or leave blank to exit): ")
    
    if name == "":
        break  # Exit the loop if the name is an empty string
    
    practical = float(input("Enter the practical grade (0-10): "))
    problem = float(input("Enter the problem grade (0-10): "))
    theoretical = float(input("Enter the theoretical grade (0-10): "))
    
    if 0 <= practical <= 10 and 0 <= problem <= 10 and 0 <= theoretical <= 10:
        final_grade = 0.10 * practical + 0.50 * problem + 0.40 * theoretical
        student_data.append({"Name": name, "Final Grade": final_grade})
    else:
        print("Error: Grades must be between 0 and 10. Please try again.")

# Display the final grades for all students
for student in student_data:
    name = student["Name"]
    grade = student["Final Grade"]
    print(f"{name}: Final Grade = {grade:.2f}")
