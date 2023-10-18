while True:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    if num1 == 0 and num2 == 0:
        break  # Exit the loop if both numbers are 0
    
    sum_result = num1 + num2
    print(f"The sum of {num1} and {num2} is {sum_result}")
