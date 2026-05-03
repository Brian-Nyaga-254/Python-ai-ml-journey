""" with open("names.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip()) """

"""
creates a list
Reads the file and appends while stripping the new line
sorts the names and the prints the output
reversed from z to a
"""
names = []
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello,{name}")       