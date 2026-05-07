"""
This program capitalizes wrestlers name that the user inputs 
And prints their description
The program uses match statement to group the names
"""
name = input("Enter a name: ").title()
match name:
    case "Roman Reigns":
        print("The Tribal Chief")
    case "John Cena":
        print("The Face that Runs the Place")
    case "Randy Orton":
        print("The viper")
    case _:
        print("Who ?")

                
