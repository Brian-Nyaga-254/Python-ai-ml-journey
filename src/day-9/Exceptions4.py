def main():
    x = get_int("What is x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            pass

main()
