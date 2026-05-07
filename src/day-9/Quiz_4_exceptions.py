"""
A program that has a function get_integer()
keeps asking the integer untill valid
and returns the integer
Has a main function that calls get_integer()
Prints the square of the returned number
"""
def main():
    x = get_integer()
    square = x * x
    print(f"The square of {x} is {square}")
    
def get_integer():
    while True:
        try:
            x = int(input("Enter an integer: "))
            return x
        except ValueError:
            print("Please enter an integer.")
            pass
       

main()