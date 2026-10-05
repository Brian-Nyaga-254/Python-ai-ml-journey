class Student:
    def __init__(self, first, middle, last,house):
        
        if not middle:
            raise ValueError("Missing Second Name")
        #instance variables
        self.first = first
        self.middle = middle
        self.last = last
        self.house = house
    
    def __str__(self):
        return f"{self.first} {self.middle} {self.last} is from {self.house}"
    
    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, first):
        if not first:
            raise ValueError("Missing first name")
        self._first = first


    #getter
    @property
    def house(self):
        return self._house
    
    #setter
    #self._house to avoid collision with init method self.house
    @house.setter
    def house(self, house):
        if house not in ["Kenya", "Embu"]:
            raise ValueError("Invalid house")
        self._house = house
    
def main():
    student = get_student()
    """ student.house = "Lionel Messi" """
    print(student)
"""student.house = 'Lionel Messi' overrides the if condition.Getter and Setter fixes this problem
when you run student.house = "Lionel Messi" with getter and setter applied valueerror which you have assigned will be displayed """




def get_student():

    first = input("First Name: ").title()
    middle = input("Middle Name: ").title()
    last = input("Last Name: ").title()
    house = input("House: ").title()
    return Student(first, middle, last, house)

if __name__ == "__main__":
    main()