"""
Using Dictionaries in Python

A dictionary stores data as key-value pairs.
"""

# First position -> Key
# Second position -> Value
Dict = {"sam": 78695087, "jon": 89675847, "alex": 7859485674, "Jay": 9908776754}

# Printing the dictionary
print(Dict)

# Deleting a key-value pair from the dictionary
# Here we remove the entry for alex
print('Removing alex from the dictionary...')
del Dict["alex"]
print(Dict)

# Looping through the dictionary and printing each key-value pair
for key in Dict:
    print("Key:", key, "Value", Dict[key])

print('------------')
print()

# Printing the dictionary items as pairs
print(Dict.items())

