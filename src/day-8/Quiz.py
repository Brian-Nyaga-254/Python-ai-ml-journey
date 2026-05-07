def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
        elif n == 0 or n < 0 :
            print("ERROR! Enter a positive number")

        

    return n
          
def Goated(n):
    for _ in range(n):
        print("Roman reigns is the tribal chief") 

def main():
    number = get_number()
    Goated(number)

main()        