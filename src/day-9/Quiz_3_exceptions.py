"""
A program that repeatedly asks for an integer
Stops only when valid
prints the number inputted
"""
while True:
    try:
        number = int(input("Enter a integer: "))
        print(f"Valid number entered: {number}")
        break
    except ValueError:
        print("Invalid input.Please enter a whole number")
    
        

