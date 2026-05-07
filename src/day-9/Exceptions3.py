def main():
    x = get_int()
    print(f"X is {x}")
def get_int():
    while True:
        try:
            x = int(input("What is x? "))
        except ValueError:
            print("X is not an integer")    
        else:
            break
    return x
    
main()