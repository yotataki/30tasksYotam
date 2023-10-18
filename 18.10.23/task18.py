# Prompt the user to enter a natural number
n = int(input("Enter a natural number: "))

# Initialize the factorial to 1
factorial = 1

# Calculate the factorial of the number
for i in range(1, n + 1):
    factorial *= i

# Display the result
print(f"The factorial of {n} is: {factorial}")
