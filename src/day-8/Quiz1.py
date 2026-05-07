"""
A program that asks user for a number between 1 and 10
prints valid number once correct
"""
number = int(input("Enter a number between 1 and 10: "))
while True:
    if number < 1 or number > 10:
        number = int(input("Invalid number. Enter a number between 1 and 10: "))
    else:
        print("Valid number")
        break    
