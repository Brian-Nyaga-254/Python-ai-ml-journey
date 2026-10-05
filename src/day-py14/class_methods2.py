class Footballer:
    def __init__(self, name, age, nationality, team):
        self.name = name
        self.age = age
        self.nationality = nationality
        self.team = team

    def __str__(self):
        return f"{self.name} is {self.age} years old from {self.nationality} and plays for {self.team}"
    
    @classmethod
    def get(cls):
        name = input("Enter the footballers name: ").capitalize()
        age = int(input("Enter age of the footballer: "))
        nationality = input("Enter nationality of the player: ").capitalize()
        team = input("Enter the team the player currently plays in: ").capitalize()
        return cls(name, age, nationality, team)



def main():
    player = Footballer.get()
    print(player)



if __name__ == "__main__":
    main()