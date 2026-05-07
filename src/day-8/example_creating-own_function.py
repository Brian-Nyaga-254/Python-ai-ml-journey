def main ():
    number = get_number()
    num(number)

def get_number ():
    while True:
        n = int(input("Enter a positive number: "))
        if n <= 0:
            continue
        else:
            break
    return n

def num(n):
    for _ in range (n):
        print("The Tribal chief is Roman Reigns ")   

main()             