"""
A python program that asks user for 3 decimal numbers
converts then into float
computes the average
and prints the results rounded to 2 decimal places
"""
x = float(input("Enter first decimal number: "))
y = float(input("Enter second number: "))
z = float(input("Enter third number: "))
average = (x + y + z)/2
print(f"{average: .2f}")
