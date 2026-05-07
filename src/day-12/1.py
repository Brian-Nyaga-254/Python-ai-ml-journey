import csv

# Open file once before the loop
with open("student_grade.csv", "a", newline="") as file:
    writer = csv.writer(file)
    
    while True:
        name = input("Enter your name (or 'quit' to stop): ")
        
        if name == "quit":
            break
        
        subject = input("Enter the subject name: ")
        grade = int(input("Enter the grade: "))
        
        writer.writerow([name, subject, grade])
        print(f"Saved: {name}, {subject}, {grade}\n")

print("All data saved to students_grade.csv")