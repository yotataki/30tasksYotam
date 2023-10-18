# Initialize an empty list to store the multiples of 2 or 3
multiples = []

# Iterate through numbers from 1 to 100
for num in range(1, 101):
    # Check if the number is a multiple of 2 or 3
    if num % 2 == 0 or num % 3 == 0:
        multiples.append(num)

# Print the numbers that are multiples of 2 or 3
for multiple in multiples:
    print(multiple)

# Flowchart:
# [Start]
#   |
#   V
# Initialize an empty list 'multiples'
#   |
#   V
# For 'num' in range(1, 101):
#   |
#   V
#   |--- Is 'num' a multiple of 2 or 3? --- No --|
#   |                                        |    |
#   |                                        |    |
#   |----------------------------------------|    |
#   |                                         Yes  |
#   |                                         |    |
#   V                                         V    |
# Append 'num' to 'multiples'                   |
#   |                                         |
#   V                                         |
# End of loop -----------------------------|
#   |
#   V
# For each 'multiple' in 'multiples', print 'multiple'
#   |
#   V
# [End]
