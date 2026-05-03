"""
A python program that defines a function to add two integers
Asks user to input the two integers and prints their sum
"""
def add(a,b):
    return a + b
    
def main():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    print(f"The sum of {a} and {b} is: {add(a,b)}")

 
main()    