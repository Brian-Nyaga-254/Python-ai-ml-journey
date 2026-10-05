""" You are writing a program to manage student records. Create three functions that work together:
get_student_info() - A function that:
Prompts for a student's name (input: "Student name: ")
Prompts for their grade (input: "Grade (0-100): ")
grade =s both values as a tuple
determine_letter_grade(score) - A function that:
Takes a numerical grade as a parameter
Returns the letter grade based on:
90-100: "A",80-89: "B",70-79: "C",60-69: "D",Below 60: "F"
display_student(name, letter_grade) - A function that:
Takes a student name and letter grade
Prints: "[Name] earned a [Letter Grade]"
Finally, write a main() function that:
Calls get_student_info() to get name and score
Calls determine_letter_grade() to convert the score
Calls display_student() to show the result """
def main():
    name, grade = get_student_info()
    letter_grade = determine_letter_grade(grade)
    display_student(name, letter_grade)

def get_student_info():
    name = input("Enter your name: ").title()
    grade = int(input("Enter your grade:(0-100)"))
    return(name,grade)
#parameters eg grade in determine_letter_grade(grade) allow data to flow into functions
# return allows data to flow out of functions 
def determine_letter_grade(grade):
    if grade>=90 and grade<=100:
        return "A"
    elif grade>=80 | grade<=89:
        return "B"
    elif grade>=70 and grade<=79:
        return "C"
    elif grade>=60 and grade<=69:
        return "D"
    else:
        return "F"
def display_student(name, letter_grade):
    print(f"{name} earned a {letter_grade}")

if __name__ =="__main__":
    main()