# Functions in Python
def greet(name):
    print(f"Hello, {name}!")
    print("Welcome to Python!")

# Call the function
greet("Alice")

# Function with parameters
def greet_student(name, dept):
    greet(name)
    print(f"Welcome {name}, from the department of {dept}!")

greet_student("Bob", "Computer Science")

# Function with Logic
def calculate_area_circle(radius):
    import math
    area = math.pi * (radius ** 2)
    return area

print(calculate_area_circle(5))

def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

check_weather()

# Variable scope: Global vs Local
# Local scope
def calculate_price():
    price = 100
    tax = price * 0.1
    print(f"Total: {price + tax}")

calculate_price()  # Total: 110
# This fails - price doesn't exist outside the function
# print(price)  # NameError: name 'price' is not defined

# Global scope
discount_rate = 0.15  # Global variable

def apply_discount(price):
    discount = price * discount_rate  # Can read global variable
    return price - discount

result = apply_discount(100)
print(result)  # 85.0

# Modifying a global variable inside a function
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2
# NOTE: Avoid using global when possible. It makes code harder to understand and debug. Instead, pass values as parameters and return results.
