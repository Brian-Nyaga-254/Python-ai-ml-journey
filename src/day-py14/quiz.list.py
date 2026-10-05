""" Rewrite the get_student() function to return a mutable data type that allows score updates. Then modify the code so that:
Student gets 5 bonus points added to their score
If the student's name is "Alice", give her an additional 10 points (15 total bonus)
Print the final result """
def main():
    name, marks = get_student()
    mark = marks + 5
    if name == "Alice":
        mark = mark + 10 
    print(f"{name} has {mark}")

    

def get_student():
    name = input("Enter your name: ")
    marks = int(input("Enter your grade: "))
    return([name,marks])

if __name__ == "__main__":
    main()