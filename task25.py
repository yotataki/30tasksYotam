# Define the correct access code
correct_code = "1234"

# Use a while loop to repeatedly ask for the access code
while True:
    user_code = input("Enter the access code: ")
    
    if user_code == correct_code:
        print("Access granted.")
        break  # Exit the loop if the correct code is entered
    else:
        print("Access denied. Please try again.")
