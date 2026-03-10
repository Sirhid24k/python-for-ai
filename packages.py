# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)
print(math.sqrt(64))

# Pattern 2: Import specific items from a module
from math import sqrt, pi
# Now use: sqrt(16)
print(sqrt(81))
print(pi)

# Built-in Modules
# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])
print(number, choice)

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)
print(json_string)  # {"name": "Alice", "age": 30}

# Import with alias
import pandas as pd
# df = pd.DataFrame(data)

# Import everything (avoid this!)
# from math import *

# Installing third-party packages
# Install a package
# pip install requests

# Install specific version
# pip install requests==2.28.0

# Install multiple packages
# pip install pandas numpy matplotlib

# Sharing your project: requirements.txt
# Creating requirements.txt
# pip freeze > requirements.txt

# Installing from requirements.txt
# pip install -r requirements.txt

# Using external packages
# Web requests
# import requests

# response = requests.get("https://api.example.com/data")
# data = response.json()

# Data analysis
import pandas as pd

# Create a simple DataFrame
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)
print(df)