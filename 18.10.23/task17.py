# Prompt the user to enter the number N
N = int(input("Enter a number N: "))

# Initialize variables to keep track of the largest number and its position
largest_number = None
largest_position = None

# Iterate through the numbers entered by the user
for position in range(1, N + 1):
    num = int(input(f"Enter number {position}: "))
    
    # Check if the current number is larger than the previously largest number
    if largest_number is None or num > largest_number:
        largest_number = num
        largest_position = position

# Display the result
print(f"The largest number is {largest_number} in the {largest_position} position.")
