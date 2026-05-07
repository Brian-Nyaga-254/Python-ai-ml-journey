""" with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
       print(f"{row[0]} is in {row[1]}") 
       
       name, house = line.rstrip().split(",")
       print(f"{name} is in {house}") """


students = []
with open ("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")  
        """students.append(f"{name} is in {house}")
        for student in sorted(students):
            print(student) """

        """dictionary that reads students.csv
        student{}
        student["name"]=name
        student["house"]=house
        student = {"name": name, "house": house}
        """
        student = {"name": name, "house": house}
        students.append(student)

"""
create a function that returns name inorder to sort items in the dictionary
 def get_name(student):
    return student["name"]

for student in sorted (students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}") """
"""Lambda is equivalent to the get_name function
   it acts as a function with no name
"""
for student in sorted (students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")        