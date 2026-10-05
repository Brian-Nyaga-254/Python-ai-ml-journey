

def main():
    student = get_student()
    if student["name"] == "brian":
       student["house"] = "kenya" 
       
    print(f"{student['name']} from {student['house']}")

def get_student():
   """  student = {}
    student["name"] = input("name")
    student["house"] = input("house")
    return student """
   
   name = input("Name: ")
   house = input("House: ")
   return {"name": name, "house": house}


if __name__ == "__main__":
    main()


    