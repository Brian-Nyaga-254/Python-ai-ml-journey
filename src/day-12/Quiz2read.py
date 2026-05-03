""" Task: Write code that:

Reads all names from the file

Prints only names that have 5 or more letters

Each name should be printed as "Welcome, [name]!" """

with open("class.txt") as file:
    lines=file.readlines()
for line in lines:
    if len(line.rstrip()) >= 5:
        print("Welcome,",line.rstrip())