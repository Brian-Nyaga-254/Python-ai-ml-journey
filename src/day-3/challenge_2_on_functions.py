"""
This is a simple Python script that defines a function to greet a user by name.
"""

def say_hello(name):
    print("Hello,", name)
user_name = input("What is your name: ").strip().title()
say_hello(user_name)


    