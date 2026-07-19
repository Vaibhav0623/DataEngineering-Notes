"""
Using Tuples in Python

A tuple is a collection of values grouped together.
Tuples are immutable, meaning they cannot be changed after creation.

# Creating a tuple with different data types
# The values can be numbers, strings, booleans, and more

tup1 = (6, 7, 8, 5, "xbnv", True, "ja")

# Printing the full tuple
print(tup1)

# Accessing an item at a specific index
print(tup1[3])


# Count an Element

numbers = (10,20,30,20,40,20)

"""

# Find The largest Number
numbers = (15, 42, 8, 99, 23)

largest = numbers[0]

for i in numbers:
    if i > largest:
        largest = i

print("Largest number =", largest)

# Counting Numbers
count_num = 0

for i in numbers:
    if i == 20:
        count_num += 1
print('20 appears',count_num,'times')

# Convert tuples to list

fruits = ("apple", "banana", "mango")

fruit_list = list(fruits)

print(fruit_list)

# Print Index With Element

colors = ("Red", "Green", "Blue", "Yellow")
j = 0

for i in colors:
    print('Index',j,' :',i)
    j +=1

# Find The Comman element

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (3, 4, 5, 6, 7)

for i in tuple1:
    if i in tuple2:
        print(i)
