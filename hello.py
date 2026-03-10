import requests

response = requests.get('https://api.github.com')
print(response.status_code)

# Variables
name = 'Alice'
is_student = True
age = 25

print(f"Hello, {name}, How are you doing!")

"""
This is a multi-line comment.
It can span multiple lines.
"""
# Data types
# String, Integer, Float, Boolean, List, Tuple, Dictionary
# String
greeting = "Hello, world!"
greeting.lower()
greeting.upper()
greeting.title()
greeting.replace("World", "Alice")

# Numbers and operations
# Integer
age = 25
# Float
price = 20.5
tax = price * 0.1
total_price = tax + price
print(f"Total price is {total_price}")

# Boolean
is_student = True
is_logged_in = False
print(age == 20)
print(age >= 20)
print(age < 12)
print(age != 31)

# Logical operators
person_age = 25
has_license = True

# AND operator - both must be true
can_drive = person_age >= 18 and has_license
print(can_drive) # True

# OR operator - either can be true
can_drive = person_age >= 18 or has_license
print(can_drive) # True

# NOT operator - inverts the boolean value
cannot_drive = not can_drive
print(cannot_drive) # False

# Conditional statements
temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("It's warm outside.")
else:
    print("It's cold outside.")

# Loops
# For loop
for i in range(5):
    print(i) # 0, 1, 2, 3, 4

# Count from 1 to 5
for i in range(1, 6):
    print(i) # 1, 2, 3, 4, 5

# Count by 2s from 0 to 10
for i in range(0, 10, 2):
    print(i) # 0, 2, 4, 6, 8

