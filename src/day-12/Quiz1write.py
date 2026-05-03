""" Task: Write code that:

Reads all the names from the file

Prints "Hello, [name]" for each name (one per line) """

students=input("Enter name of the student: ")
file = open("student.txt", "a")
file.write(f"{students}\n")
file.close()