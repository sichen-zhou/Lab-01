# Input Info
name = input("What is your name? ")
birth_year = input("What is the year of your birth? ")

# Age Calculation
from datetime import datetime
this_year = datetime.now().year
age = this_year - int(birth_year)

# Output Statements
print(f"Hello, {name}!")
print(f"You must be {age}.")