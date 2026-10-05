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
   
    


def main():
    player = get_footballer_name()
    print(f"{player.name} is currently {player.age} years old,Player is from {player.nationality} and currently plays for {player.team}")

def get_footballer_name():
   
    name = input("Enter the footballers name: ").capitalize()
    age = int(input("Enter age of the footballer: "))
    nationality = input("Enter nationality of the player: ").capitalize()
    team = input("Enter the team the player currently plays in: ").capitalize()
    player = Footballer(name, age, nationality, team)
    return player

if __name__ == "__main__":
    main()
