# Prompt the user to enter a grade
grade = int(input("Enter a grade (1-10): "))

# Validate that the grade is between 1 and 10
if 1 <= grade <= 10:
    if grade >= 9:
        print("You have obtained an outstanding grade.")
    elif 7 <= grade <= 8:
        print("You have obtained a notable grade.")
    elif 4 <= grade <= 6:
        print("You have obtained a pass.")
    else:
        print("You have disapproved.")
else:
    print("Invalid grade. Please enter a grade between 1 and 10.")
