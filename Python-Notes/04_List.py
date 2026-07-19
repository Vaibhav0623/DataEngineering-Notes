"""
Using Lists in Python 

All The Value Have Same meaning

Note: List are mutable, meaning you can change their content without changing their identity. Lists are ordered collections of items (which can be of different types) and are defined by square brackets [].
"""

Items = ["bread","pasta","fruits","veggies"]

print(Items)

print()

print('After Changing the first item')

Items[0] = "cheese" # Changing the first item

"""
print(Items)

print(Items[0:3]) # Slicing the list to get the first three items

print(Items[2:]) # Slicing the list to get all items from index 2 to the end
"""

Items.append("milk") # Adding an item to the end of the list

print(Items)

Items.insert(3,"butter") # Inserting an item at index 3
print(Items)

Items.remove("fruits") # Removing an item from the list
print(Items)

print(len(Items)) # Getting the length of the list

Items.sort() # Sorting the list in ascending order
print(Items)

Items.reverse() # Reversing the order of the list
print(Items)

"""
Items.clear() # Clearing all items from the list
print(Items)
"""

Items.pop() # Removing the last item from the list
print(Items)

Food_items = ["bread","pasta","fruits","veggies"]
Bathroom_items = ["soap","shampoo","toothpaste"]

Items_List = Food_items + Bathroom_items # Concatenating two lists
print(Items_List)

# Finding the Item in List

print("bread" in Food_items)

