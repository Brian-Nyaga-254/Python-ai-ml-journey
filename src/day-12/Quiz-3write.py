"""
Ask the user to enter student information (name, subject, grade)
Continue asking until the user enters "quit" for the name
Save all entries to a file called student_grades.csv using csv.DictWriter
Include headers: "name", "subject", "grade"
"""
import csv

name = input("Enter your name: ")
subject = input("Enter the subject name: ")  
grade = int(input("Enter the grade: "))

with open("student_grade.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "subject", "grade"])
    writer.writerow({"name": name, "subject": subject, "grade": grade})
"""    writer = csv.writer(file)
   writer.writerow([name,subject,grade]) """
print("Information saved succesfully")
    
            
          
    
