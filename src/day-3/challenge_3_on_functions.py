"""
This is a python script that defines a function to welcome users in general
and also welcomes a specific user when a name is provided.
"""
def welcome(name = "Guest"):
    print("Welcome,", name)
    
    
welcome()

user_name = input("Please enter your name: ").strip().title()
welcome(user_name)   