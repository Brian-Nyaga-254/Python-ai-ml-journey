def main():
    action = input("Do you want to (enroll) or (drop) a student? ")
    if action == "enroll":
        student = enroll_student()
    elif action == "drop":
        student = drop_student()
    print(student)


def  get_student_info():
    name = input("Enter your name: " )
    course = input("Enter your course: ")
    year = int(input("Enter the year you enrolled: "))
    enrolled = input("Enrolled (True/False): " )
    if enrolled == "True":
        enrolled = True
    else:
        enrolled = False

    return {"name": name,"course": course,"year": year,"enrolled": enrolled}
    

def enroll_student():
     # FIRST: Get the student info by calling the function
    student = get_student_info() # This returns a dictionary


    if student["enrolled"] == "True":
        print("Student is already enrolled in this course")
    else:
        student["enrolled"] = True
        print("Student succesfully enrolled")
    return student

def drop_student():
    student = get_student_info()
    if student["enrolled"] == "True":
        student["enrolled"] = False
        print("Student has been dropped from the course")
    else:
        print("Student is not currently enrolled")
        return student
    
if __name__ =="__main__":
    main()

    
 #when using dictionaries to access values use[] instead of ()   
    

 