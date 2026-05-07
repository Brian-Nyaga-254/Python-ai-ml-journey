"""
This program capitalizes footballers name that the user inputs 
And prints their description
The program uses if, elif and else to group the names
"""

name = input("Enter a name: ").title()
if name == "Lionel Messi":
    print("You entered the name of the football goat!")
elif name == "Cristiano Ronaldo":
    print("You have chosen a football legend!")
elif name == "Neymar Jr":
    print("You have selected the football prince!")
elif name == "Mohamed Salah":
    print("You picked the Egyptian King of Football!")    
else:

    print("Who ?")    
