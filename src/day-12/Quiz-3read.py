"""
Ask the user to enter student information (name, subject, grade)
Continue asking until the user enters "quit" for the name
Save all entries to a file called student_grades.csv using csv.DictWriter
Include headers: "name", "subject", "grade"
"""

import csv
student=[]
with open("student_grade.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        student.append(row)
        
        
        """  key=lambda students: int(students["grade"])
         incase you want to use grade and you want them sorted as numbers """
for students in sorted(student, key=lambda students:students["name"]):
    print(f"{students['name']} scored in {students['subject']} {students['grade']}")