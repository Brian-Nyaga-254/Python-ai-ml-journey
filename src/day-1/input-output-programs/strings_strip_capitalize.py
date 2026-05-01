"""
A program that removes whitespaces 
And capitalizes users input
"""
#Ask user to input their name
name = input('What is your name? ')
#Greet the user with their name
name = name.strip()
name = name.capitalize()

print('Hello,' , name , end = '',)


