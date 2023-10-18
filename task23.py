# Initialize variables for maximum, minimum, sum, and count
max_value = float('-inf')  # Set to negative infinity as the initial max
min_value = float('inf')   # Set to positive infinity as the initial min
sum_values = 0
count = 0

# Continue to read integers until the user types 0
while True:
    num = int(input("Enter an integer (0 to stop): "))
    
    if num == 0:
        break  # Exit the loop if the user types 0
    
    # Update maximum and minimum values
    max_value = max(max_value, num)
    min_value = min(min_value, num)
    
    # Update sum and count
    sum_values += num
    count += 1

# Calculate the average
average = sum_values / count if count > 0 else 0

# Display the results
print(f"Maximum: {max_value}")
print(f"Minimum: {min_value}")
print(f"Average: {average}")

# Flowchart:
# [Start]
#   |
#   V
# Initialize max_value to negative infinity
# Initialize min_value to positive infinity
# Initialize sum_values to 0
# Initialize count to 0
#   |
#   V
# [Loop]
#   |
#   V
# Prompt the user to enter an integer
#   |
#   V
# Check if the user entered 0 -- No ->|
#   |                                |
#   |                                Yes
#   V                                |
#   |                                |
#   |                                V
#   |                                |
#   |                                |
#   |--- Update max_value and min_value
#   |                                |
#   |                                |
#   |--- Update sum_values and count
#   |                                |
#   |                                |
#   V                                |
#   |
# [Exit if user types 0]
#   |
#   V
# Calculate the average (if count is greater than 0)
#   |
#   V
# Display the maximum, minimum, and average
#   |
#   V
# [End]
