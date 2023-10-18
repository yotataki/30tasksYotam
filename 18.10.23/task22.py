# Define the correct key
correct_key = "eureka"

# Initialize the number of attempts
attempts = 0

# Set the maximum number of attempts
max_attempts = 3

# Use a while loop to allow the user to make up to three attempts
while attempts < max_attempts:
    # Prompt the user to enter a clue
    clue = input("Enter a clue: ")
    
    # Check if the entered clue matches the correct key
    if clue == correct_key:
        print("Congratulations! You've found the correct key (eureka).")
        break  # Exit the program
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Clue does not match. You have {remaining_attempts} attempt(s) remaining.")

# Check if the user exhausted all attempts
if attempts == max_attempts:
    print("You have exhausted all 3 attempts. Access denied.")
