"""
This program takes three numbers from the users and checks wether:
-All are equal
-Two are equal
-All are different
"""
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b == c:
    print("All equal")
elif a == b != c or b == c != a or a == c != b:
    print("Two equal")
else:
    print("All different")    

