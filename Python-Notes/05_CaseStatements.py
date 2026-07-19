"""
Using Conditional Statements in Python

This file demonstrates simple if-else and elif logic.
"""

# Example 1: Check whether a number is even or odd
num = int(input("Enter a Number: "))

if num % 2 == 0:
    print("The number is even.")
elif num % 2 != 0:
    print("The number is odd.")
else:
    print("Enter a Valid Number.")

# Example 2: Identify the cuisine of a dish
indian = ["samosa", "daal", "vada pav"]
italian = ["pasta", "pizza", "risotto"]
chinese = ["fried rice", "pot sticker"]

dish = input("Enter a Dish Name: ")

if dish in indian:
    print("The dish is Indian.")
elif dish in italian:
    print("The dish is Italian.")
elif dish in chinese:
    print("The dish is Chinese.")
else:
    print("I don't know which cuisine is", dish)

# Example 3: Check voting eligibility
Age = int(input("Enter Your Age: "))

if Age > 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

