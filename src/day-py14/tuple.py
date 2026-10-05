def main():
    name, house = get_student()
    
    """ name = get_name()
    house = get_house() """
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house) 
    """a tuple grouping name and house since we are not changing them"""

""" 
def get_name():
    return input("Name: ")
def get_house():
    return input("House: ") """

if __name__ == "__main__":
    main()
    