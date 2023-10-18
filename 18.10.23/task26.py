# Define the correct username and password
correct_username = "admin"
correct_password = "1234"

# Use a while loop to repeatedly ask for credentials
while True:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if username == correct_username and password == correct_password:
        print("Access granted.")
        break  # Exit the loop if the correct credentials are entered
    else:
        print("Access denied. Please try again.")

# Flowchart:
# [Start]
#   |
#   V
# Define the correct username as "admin"
# Define the correct password as "1234"
#   |
#   V
# [Loop]
#   |
#   V
# Prompt the user to enter their username
#   |
#   V
# Prompt the user to enter their password
#   |
#   V
# Check if the entered username and password match the correct credentials -- No --|
#   |                                                                            |
#   |                                                                            Yes
#   V                                                                            |
#   |                                                                            |
#   |--- Display "Access denied. Please try again."                            |
#   |                                                                            |
#   |                                                                            |
#   V                                                                            |
#   |                                                                            |
# [Exit if correct username and password are entered]                            |
#   |                                                                            |
#   V                                                                            |
# Display "Access granted."                                                    |
#   |                                                                            |
#   V                                                                            |
# [End]
