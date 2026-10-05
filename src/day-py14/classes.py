"""
 def __init__(self, first, middle, last,house): IT IS AN INSTANCE METHOD
The constructor METHOD that automatically runs when creating a new Student object. __init__ stands for "initialize".
self refers to the specific object being created
first, middle, last, house are parameters that must be provided,they are instance variables


"""

class Student:
    def __init__(self, first, middle, last,house):
        if not first:
            raise ValueError("Missing First name")
        if not middle:
            raise ValueError("Missing Second Name")
        if house is not None and house not in ["Kenya", "Embu"]:
            raise ValueError("Invalid house")
        self.first = first
        self.middle = middle
        self.last = last
        self.house = house

    def __str__(self):
        return f"{self.first} {self.middle} {self.last} is from {self.house}"
    
    def third(self):
        match self.last:
            case "Mugai":
                return"😶‍🌫️"
            case "Nyaga":
                return"👌"
            case "Brian":
                return "😤"
            case _:
                return"😒"




def main():
    student = get_student()   
    """ print(f"{student.first},{student.middle},{student.last} from {student.house}") """
   
   
    """print(student) without --str-- returns file location as object in your pc"""
    """   print(student) """

    print("Your name!")
    print(student.third())

def get_student():
   """
   student is the object created
     student = Student()
   student.name = input("Name: ")
   student.house = input("House: ")
    return student
      """
   
   first = input("First Name: ")
   middle = input("Middle Name: ")
   last = input("Last Name: ")
   house = input("House: ")
   return Student(first, middle, last, house)
"""
Student() acts as a class to create objects
Student(first, middle, last, house) is a constructor call which creates the student object
"""
  
  

if __name__ == "__main__":
    main()