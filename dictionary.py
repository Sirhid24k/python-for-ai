# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "hobby": "Sightseeing"
}

# Get values by key
person["name"]
person["city"]

# Add or update
person["name"] = "Dave" # Update existing
person["license"] = True # Add new

# Remove items
del person["license"]              # Remove by key
age = person.pop("age")          # Remove and return
person.clear()                   # Remove all items

# Dictionary methods
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})

# Nested dictionaries
# Dictionary of dictionaries
students = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"},
    "charlie": {"age": 19, "grade": "A"}
}

# Access nested data
print(students["alice"]["grade"])  # "A"