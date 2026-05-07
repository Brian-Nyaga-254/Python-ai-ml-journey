"""
A program that gets a positive integer from the user
and prints "Goated" that many times using a function.
"""
def main():
    number = get_number()
    goated(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))    
        if n > 0:
            break
    
    return n

def goated(n):
    for _ in range (n):
        print("Goated")

main()
