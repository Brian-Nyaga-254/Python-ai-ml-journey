class Footballer:
    def __init__(self, name, age, nationality, team):
        if not name:
            raise ValueError("Missing name")
        if nationality not in ["Argentina", "Kenya", "Portugal"]:
            raise ValueError("Invalid Nationality")
        if age <= 0:
            raise ValueError("Age must be a positive integer")
        
        self.name = name
        self.age = age
        self.nationality = nationality
        self.team = team

    def __str__(self):
        return f"{self.name} is {self.age} years old from {self.nationality} and plays for {self.team}"
    
    def country(self):
        match self.nationality:
            case "Argentina":
                return"🐐"
            case "Kenya":
                return "🤩"
            case "Portugal":
                return"😎"
            case _:
                return"🤦‍♂️"
   
    


def main():
    player = get_footballer_name()
    print("gooooooo")
    print(player.country())

def get_footballer_name():
   
    name = input("Enter the footballers name: ").capitalize()
    age = int(input("Enter age of the footballer: "))
    nationality = input("Enter nationality of the player: ").capitalize()
    team = input("Enter the team the player currently plays in: ").capitalize()
    player = Footballer(name, age, nationality, team)
    return player

if __name__ == "__main__":
    main()
