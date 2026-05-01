"""
Ask the user for their name
Remove extra spaces from the beginning and end
Capitalize the name
Print two lines of output:
"""
name = input("What is your name: ")
name = name.strip()
name = name.capitalize()
print(f"Hello {name}", end="\n")
print("Welcome to the system")

