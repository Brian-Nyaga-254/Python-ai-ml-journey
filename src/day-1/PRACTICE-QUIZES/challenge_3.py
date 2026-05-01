"""
Ask the user for their name
Remove leading and trailing spaces
Capitalize the name
"""
name = input("What is your name? ")
name = name.strip()
name = name.capitalize()
print(f"Hello {name}", end = "\n")
print("Welcome")


