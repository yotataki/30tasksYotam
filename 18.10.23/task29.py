# Define the names of months
months = ["", "January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# Prompt the user to enter the date components
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

# Check if it's a valid date
if 1 <= month <= 12 and 1 <= day <= 31 and year > 0:
    print(f"{months[month]}, {day}, {year}")
else:
    print("Error: Invalid date entered.")
