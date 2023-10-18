# Step 1: Prompt the user to enter a symbol
symbol = input("Enter a symbol to draw the square: ")

# Step 2: Prompt the user to enter the size of the square
size = int(input("Enter the size of the square: "))

# Step 3: Start a loop to draw the square
for _ in range(size):  # Step 4
    print(symbol * size)
