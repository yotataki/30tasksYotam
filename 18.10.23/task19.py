# Prompt the user to enter the side length of the square
side = int(input("Enter the side length of the square: "))

# Check if the side length is at least 2
if side >= 2:
    # Print the top edge of the square
    print("*" * side)

    # Print the middle rows of the square
    for _ in range(side - 2):
        print("*" + " " * (side - 2) + "*")

    # Print the bottom edge of the square
    print("*" * side)
else:
    print("Please enter a side length of at least 2 to create a valid square.")
