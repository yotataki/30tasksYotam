# Algorithm:
# [Start]  -->  (1) Prompt the user to enter an integer
#   |       |
#   v       |
# [Input]   |
#   |       |
#   v       |
# (2) Read and store the integer
#   |       |
#   v       |
# (3) Check if the integer is even or odd
#   |       |
#   v       |
# [Is integer % 2 == 0?]  -->  [Even]  -->  (4) Display "The number is even."
#   |       |  (Yes)         |  (Yes)       |
#   |       |                |              |
#   |       v                |              |
#   |     [Output]  <-----------------------
#   |       |
#   |       |
#   |       v
#   |     [Even]
#   |       |
#   |       v
#   |     (5) Display "The number is odd."
#   |       |
#   |       |
#   v       |
# [Output]  <--------  [Odd]  -->  (6) Display "The number is odd."
#             (No)           (No)

# Step 1: Prompt the user to enter an integer
num = int(input("Enter an integer: "))

# Step 3: Check if the integer is even or odd
if num % 2 == 0:  # Step 4: If the remainder when divided by 2 is 0, it's even
    print("The number is even.")
else:  # Step 6: If not, it's odd
    print("The number is odd.")
