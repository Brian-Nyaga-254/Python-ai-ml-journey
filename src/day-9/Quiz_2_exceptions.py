"""
A program that asks for 2 numbers
divides first by second
prints the results rounded to 2 decimal places
"""
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    division = num1 / num2
    print(f"Division is {division:.2f}")
except ValueError:
    print("Invalid input.Please enter numbers")  
except ZeroDivisionError:
    print("ERROR! Cannot divide by zero!")  


