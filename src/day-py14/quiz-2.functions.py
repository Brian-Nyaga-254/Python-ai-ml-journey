def main():
    name , age = get_student()
    print(f"{name} is {age} yrs old.")


def get_student():
    name = input("Enter your name: ").title()
    age = int(input("Enter your age: "))
    return name, age

main()