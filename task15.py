# Prompt the user to enter the value of N
N = int(input("Enter a positive integer N: "))

# Initialize the sum to 0
total = 0

# Calculate the sum of the first N natural numbers
for i in range(1, N + 1):
    total += i

# Display the result
print(f"The sum of the first {N} natural numbers is: {total}")
