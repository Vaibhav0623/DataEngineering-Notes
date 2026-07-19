"""
Using Loops in Python

This file demonstrates how loops can repeat actions and process multiple values.
"""

# Example 1: Add numbers in a list using a for loop
num = [4, 76, 34, 51, 23]
total = 0

for i in num:
    total += i
print("The Total is:", total)

# Example 2: Print even numbers from 1 to 20
# This collects all even values in a new list
even = []

for i in range(1, 21):
    if i % 2 == 0:
        even.append(i)

print(even)

# Example 3: Use range with a step size
for i in range(1, 11, 3):  # start, stop, and step size
    print(i)

# Example 4: Use break to stop the loop when the key is found
key_location = ["chair"]
location = ["table", "sofa", "bed", "chair", "desk"]

for i in location:
    if i == key_location[0]:
        print("Key Found")
        break
    else:
        print("Key Not Found in:", i)

# Example 5: Use continue to skip even numbers
for i in range(1, 6):
    if i % 2 == 0:
        continue
    print(i * i)

# Example 6: Print numbers using a while loop
i = 1
while i < 10:
    print(i)
    i += 1


# Print the Number From 1 to 10

for i in range(1,11):
    print(i)

# print Even Numbers From 1 to 20

for i in range(2,21,2):
        print(i)

# Find The Sum Of Numbers

Total = 0
for i in range(1,11):
    Total += i
print(Total)

# Print Each Character

text = 'python'
for i in text:
    print(i)

# Print The Square Of Numbers

for i in range(1,6):
    print(i,'square = ',i**2)


