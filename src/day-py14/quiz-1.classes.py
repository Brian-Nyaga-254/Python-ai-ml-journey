class Student:
    def __init__(self,name,course,age):
        if not name:
            raise ValueError("Missing name")
        if  not age:
            raise ValueError("Missing age")
        if course is not None and course not in ["BSE", "BSCIT", "BIT"]:
            raise ValueError("Invalid course")
        self.name = name
        self.course = course
        self.age = age

def main():
    student = student_info()
    print(f"{student.name} of age {student.age} is doing {student.course}")

def student_info():
    name = input("What is your name: ")
    course = input("Enter your course: ")
    age = int(input("Enter your age: "))
    return Student(name, course, age)

if __name__ == "__main__":
    main()

