def analyze_number(n):
    if n/2 != 0:
        print("Odd")
    else:
        print("Even")
    if n == 0:
        print("Zero")
    elif n > 0:
        print("Positive")
    else:
        print("Negative")

def main():
    n = analyze_number()
    n = int(input("Enter an integer: "))
    if n == 0:
      print("Stop") 
    elif   n/2 != 0 and n > 0:
        return n
    else:
        return n     

main()                
