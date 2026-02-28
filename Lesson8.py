import math

# Take input from user
number = float(input("Enter a number: "))

# Check if number is negative
if number < 0:
    print("Square root of a negative number is not a real number.")
else:
    result = math.sqrt(number)
    print("The square root of", number, "is", result)