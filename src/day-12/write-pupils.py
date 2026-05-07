import csv
name = input("Enter your name: ")
home = input("Enter your home: ") 

with open("pupils.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"home": home, "name": name})
"""  writer = csv.writer(file)
    writer.writerow([name, home]) """