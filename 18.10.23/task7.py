def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input: Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check if the year is a leap year using the is_leap_year function
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
