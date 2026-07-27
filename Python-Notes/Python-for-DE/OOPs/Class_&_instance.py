
# Python Object-Oriented Programming

# Creating Class

# Define a class named Employee to store employee information.

class Employee:

    def __init__(self, first, last, pay):
        # Initialize instance attributes for first name, last name, and salary
        self.first = first
        self.last = last
        self.pay = pay

        # Automatically generate an email address from the name
        self.email = first + '.' + last + '@comapny.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raises(self):
        self.pay = int(self.pay * 1.04)

# Creating Instance

# Instantiate two Employee objects with sample data.
emp_1 = Employee("Ajay", "Vyas", 50000)
emp_2 = Employee("Neha", "Jindal", 60000)

# Print the object instances. This prints the default object representation.
## print(emp_1)
## print(emp_2)

"""
emp_1.name = "Ajay"
emp_1.last = "Vyas"
emp_1.email = "Ajay.Vyas@company.com"
emp_1.pay = 50000

emp_2.name = "Neha"
emp_2.last = "Jindal"
emp_2.email = "Neha.Jindal@company.com"
emp_2.pay = 60000
"""

# Print the email address for each employee.
## print(emp_1.email)
## print(emp_2.email)


# print(emp_1.fullname())

print(emp_1.pay)
emp_1.apply_raises()
print(emp_1.pay)