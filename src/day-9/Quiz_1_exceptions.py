"""
A python program that asks the user to enter an integer
prints square of the number
prints invalid input if user does not enter an integer
"""
try:
        x = int(input("Enter an integer number: "))
        square = x * x
        print(f"The square of {x} is {square}")
except ValueError:
        print("Invalid input! Please enter a whole number.")

