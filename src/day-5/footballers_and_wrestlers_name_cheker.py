"""
This program capitalize's a name input by a user and groups them on:
Footballer or wrestler
The program uses match to group the names
"""
name = input("Enter a name: ").title()
match name:
    case "Cristiano Ronaldo" | "Lionel Messi" | "Neymar Jr" | "Mohamed Salah":
        print(f"{name} is one of the best football players in the world.")
    case "Roman Reigns" | "Randy Orton" | "John Cena" | "Brock Lesnar":
        print(f"{name} is one of the best wrestlers in the world.") 
    case _:

        print(f"Sorry, I dont have information about the person names {name}.")       
