# Step 1: Prompt the user to enter a number
num = float(input("Enter a number: "))

# Step 2: Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

"""
flow chart
Start
|
|  Step 1: Prompt the user to enter a number
|  |
|  v
| [Enter a number]
|  |
|  |
|  |
|  v
|
|  Step 2: Check if the number is positive, negative, or zero
|  |
|  v
| [Is num > 0?]
|  |
|  |
|  |
|  |------- Yes
|  |       |
|  |       v
|  |     [Print "The number is positive."]
|  |       |
|  |       |
|  |       v
|  |
|  |------- No
|  |       |
|  |       v
|  | [Is num < 0?]
|  |       |
|  |       |
|  |       |------- Yes
|  |       |       |
|  |       |       v
|  |       |     [Print "The number is negative."]
|  |       |       |
|  |       |       |
|  |       |       v
|  |       |
|  |       |------- No
|  |       |
|  |       |
|  |       |------- Yes
|  |       |       |
|  |       |       v
|  |       |     [Print "The number is zero."]
|  |       |       |
|  |       |       |
|  |       |       v
|  |       |
|  |       |------- No
|  |       |
|  |       |
|  |       v
|  |
|  v
|
End
"""