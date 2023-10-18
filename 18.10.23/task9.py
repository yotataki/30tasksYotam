# Define a list of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]

# Prompt the user to enter a month number
month_number = int(input("Enter a month number (1-12): "))

# Validate that the month number is between 1 and 12
if 1 <= month_number <= 12:
    # Convert the month number to the corresponding month name
    month_name = months[month_number - 1]
    print(f"The corresponding month is: {month_name}")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
