"""
This program classifies a number as even or odd and as positive, negative, or zero. 
Categories:
- Zero: 0
- even and odd numbers
- positive and negative numbers
- comparison of three numbers
-By creating functions for each task and using match-case for user selection.

"""

def is_even(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"
    

def number_sign(n):
    if n == 0:
        return "Zero"
    elif n > 0:    
        return "Positive"
    else:
        return "Negative"
    

def compare_three(a , b, c)    :
    if a == b == c:
        return "All equal"
    elif a == b != c or a == c != b or b == c != a:
        return "Two equal"
    else: 
        return "All different"
     


print("1.Check even or Odd \n2.Check positive,negative or zero \n3.Compare three numbers \n4.Exit \n")
selection = int(input("Enter a number between 1 and 4: "))
match selection:
    case 1:
      if selection == 1:
          number = int(input("Enter a number: "))
          result = is_even(number)
          print(result)

    case 2:
        if selection == 2:
            number = float(input("Enter a number: "))      
            result = number_sign(number)
            print(result)

    case 3:
        if selection ==  3:
            a = float(input("Enter first number: "))        
            b = float(input("Enter second number: "))
            c = float(input("Enter third number: "))
            result = compare_three(a, b, c)
            print(result)

    case 4:
        print("Goodbye")        

    case _:
        print("Invalid input!")    

