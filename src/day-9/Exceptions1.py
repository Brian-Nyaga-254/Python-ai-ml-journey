try:
    x = int(input("What is x? "))
except ValueError:
    print("X is not an integer")
else:
    print(f"x is {x}")