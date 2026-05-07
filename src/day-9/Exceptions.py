try:
    x = int(input("What is x? "))
    print(f"x is {x}")
except ValueError:
    print("X is not an integer")    