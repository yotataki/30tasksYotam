# Step 1: Prompt the user to enter three different numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Step 3: Compare the numbers to find the largest
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Step 4: Print the largest number
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")
