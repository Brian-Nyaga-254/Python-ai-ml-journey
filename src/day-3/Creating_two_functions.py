"""
This python script defines two functions:
1. square(n): This function takes a number n as input and returns its square.
2. main(): This function prompts the user to input a number, calls the square function with that number, and prints the result.
"""
def main():
    x = int(input("What is x? "))
    print("X squared is: ", square(x))



def square(n):
    return n*n

main()    