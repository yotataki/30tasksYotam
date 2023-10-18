while True:
    try:
        # Prompt the user to enter a number
        num = float(input("Enter a number: "))

        if num < 0:
            print("Error: Please enter a non-negative number.")
        else:
            # Calculate and display the square root
            square_root = num ** 0.5
            print(f"The square root of {num} is {square_root}")
            break
    except ValueError:
        print("Error: Please enter a valid number.")
