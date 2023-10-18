# Step 1: Prompt the user to enter three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Step 3: Check if the first number is negative
if num1 < 0:
    # Step 4: Calculate and print the product of the three numbers
    result = num1 * num2 * num3
    print(f"The product of the three numbers is {result}")
else:
    # Step 5: Calculate and print the sum of the three numbers
    result = num1 + num2 + num3
    print(f"The sum of the three numbers is {result}")