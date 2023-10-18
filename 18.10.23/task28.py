while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num2 == 0:
        print("Error: Division by zero. Please enter a non-zero second number.")
    else:
        result = num1 / num2
        print(f"The result of {num1} divided by {num2} is {result}")
        break
