# Prompt the user to enter the height of the inverted staircase
height = int(input("Enter the height of the inverted staircase: "))

# Check if the height is greater than or equal to 1
if height >= 1:
    for i in range(height, 0, -1):
        print("*" * i)
else:
    print("Please enter a height of at least 1 to create a valid inverted staircase.")
