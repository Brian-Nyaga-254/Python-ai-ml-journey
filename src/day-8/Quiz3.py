"""
 A program that has a function get valid age that prompts the user to enter their age.
    The function should validate that the age is a positive integer and less than or equal to 130. If the input is invalid, the function should display an error message and prompt the user to enter their age again until a valid age is entered. Once a valid age is entered, the program should print "Age Accepted: " followed by the valid age.
"""


def main():
    age = get_valid_age()
    print("Age Accepted: ",age, sep = "")



def get_valid_age () :
    while True :
        try:
            age = int(input("Enter your age: "))
            if age > 0 and age <= 130 :
                return age 
            else:
                print("INVALID AGE!Try again.")
        except ValueError :
            print("Invalid input. Enter a number") 
   

main()            




                  

    
                 
             
            
    
    
