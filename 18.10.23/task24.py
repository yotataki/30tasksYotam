even_count = 0  # Initialize the count of even numbers to 0

while True:
    num = int(input("Enter a number: "))
    
    # Check if the entered number is even
    if num % 2 == 0:
        even_count += 1

    # Ask if the user wants to enter another number
    another = input("Do you want to enter another number? [Y/N]: ").strip().lower()
    
    if another != 'y':
        break

# Display the count of even numbers
print(f"Number of even numbers entered: {even_count}")
