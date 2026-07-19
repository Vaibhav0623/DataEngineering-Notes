"""
Using Functions in Python

Functions help us reuse code and organize programs into smaller blocks.
"""

# Example 1: Create a function to calculate total expenses
jon_exp_list = [218, 543, 2334, 1278, 368]
tom_exp_list = [3221, 432, 1234, 234, 120]


def total_expenses(exp):
    total = 0
    for i in exp:
        total += i
    return total

"""
print('expenses of jon:', total_expenses(jon_exp_list))
print('expenses of tom:', total_expenses(tom_exp_list))
"""

# Example 2: Simple function to add two numbers

def sum(x, y):
    return x + y

"""
a = int(input('Enter the Number 1:'))
b = int(input('Enter the Number 2:'))
print('sum of num1 and num 2:', sum(a, b))
"""

# Example 3: Function to multiply two numbers

def prod(x, y):
    """
    This function takes two integers and returns their product.
    """
    return x * y

# Taking input from the user and calling the function
# Without arguments means the function uses user-provided values

a = int(input('Enter the Number 1:'))
b = int(input('Enter the Number 2:'))
print('Product of num1 and num 2:', prod(a, b))

# Example of passing fixed values directly
"""
print('Product of num1 and num 2:', prod(2, 3))
"""
