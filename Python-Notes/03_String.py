"""
Using Strings in Python

Note: Python strings are immutable, which means they cannot be changed after creation.
"""

# Printing a simple string
Str_1 = 'Hello World'
print(Str_1)

print('----------')

# Printing an address stored as a string
Address = 'House No.09, Slice 5, Vijay Nagar'
print('My Address:', Address)

print('----------')

# Concatenating two strings
Str_2 = 'I am Vaibhav'
Str_3 = 'I am a Python Learner'
Str_4 = Str_2 + ' and, ' + Str_3

print('Concatenated String:', Str_4)

# Indexing and slicing in strings
text = 'ice cream'
print('----------')
print(text)
print()

# Accessing characters by index
print('First character:', text[0])
print('Second character:', text[1])
print('Third character:', text[2])

# Slicing a string to get a substring
print('Slicing in strings')
print('slicing from 0 to 3:', text[0:3])

# Slicing can also include spaces in the output
print('slicing from 0 to 5:', text[0:5])
