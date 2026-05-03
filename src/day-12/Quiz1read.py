with open("student.txt") as file:
    lines=file.readlines()
for line in lines:
    print(f"Hello,{line.rstrip()}")