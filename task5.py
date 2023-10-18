def discount_by_month(month, amount):
    # Define a dictionary to map month names to their corresponding numbers.
    month_to_number = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    # Check if the input month is "October" (10).
    if month_to_number.get(month, 0) == 10:
        # Apply a 15% discount to the amount for October.
        discounted_price = amount * 0.85
    else:
        # For all other months, no discount is applied.
        discounted_price = amount

    return discounted_price

# Example usage of the function:
month = "October"
amount = 100.0
discounted_price = discount_by_month(month, amount)
print(f"Price after discount for {month}: ${discounted_price:.2f}")
