import math

# Step 1: Prompt the user to enter a number
num = float(input("Enter a number: "))

# Step 3: Check if the number is less than or equal to 0
if num <= 0:
    print("Error: The number must be greater than 0 to perform calculations.")
else:
    # Step 4: Calculate square and square root
    square = num ** 2
    square_root = math.sqrt(num)
    
    # Step 5: Display the results
    print(f"The number is {num}.")
    print(f"The square of the number is {square}.")
    print(f"The square root of the number is {square_root:.2f} (calculated using math.sqrt).")
    print(f"The square root of the number is {num ** 0.5:.2f} (calculated using power of 0.5).")
