# Step 1: Prompt the user to enter two natural numbers b and e
b = int(input("Enter the base (b): "))
e = int(input("Enter the exponent (e): "))

# Step 2: Initialize the result to 1
result = 1

# Step 3: Start a loop to calculate the result
for _ in range(e):  # Step 4
    result *= b

# Step 6: Display the result
print(f"{b}^{e} = {result}")
