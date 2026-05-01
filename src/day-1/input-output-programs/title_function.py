#Ask user to input their name
name = input('What is your name? ')
#Greet the user with their name
#remove white space from str
name = name.strip()
#capitalize user name
name = name.title()

print(f"Hello, {name}" )

