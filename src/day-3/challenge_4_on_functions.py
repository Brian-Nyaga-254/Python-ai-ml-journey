"""
A python program that defines a function square
Asks user to input a number and prints the square of that number
"""
def square(n):
    return  n*n

number =int(input("Enter a number to square: "))
print("The square of the number is:", square(number))