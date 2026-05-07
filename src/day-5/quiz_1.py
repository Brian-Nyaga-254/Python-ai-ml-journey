"""
This program classifies a number as even or odd and as positive, negative, or zero. 
"""

user_input = int(input("Choose an option between 1 and 3 \n 1.Check even or odd \n 2.Check positive or negative \n 3.Exit \n : "))
if user_input == 1:
    number = int(input("Enter a number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

elif user_input == 2:
    number = int(input("Enter a number: "))         
    if number == 0:
        print("Zero")
    elif number > 0:
        print("Positive")
    else:
        print("Negative")    

elif user_input == 3:
    print("Good bye")   

else:
    print("Invalid choice")         
