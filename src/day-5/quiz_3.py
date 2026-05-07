"""
This program classifies a number as even or odd and as positive, negative, or zero. 
Categories:
- Zero: 0
- even and odd numbers
- positive and negative numbers
"""
number = int(input("Enter a number between 1 and 3. \n 1.Check even or odd \n 2.Check positive, negative or zero \n 3.Exit \n "))
match number:
    case 1:
        number1 = int(input("Enter a number: "))
        if number1 % 2 == 0:
            print("Even") 
        else:
            print("Odd")

    case 2:
        number1 = float(input("Enter a number: "))
        if number1 == 0:
            print("Zero")
        elif number1 > 0:
            print("Positive")
        else:
            print("Negative")

    case 3:         
        print("Goodbye")

    case _:

        print("Invalid choice")    
