""" Asks the user for their name and age
Writes "Name: [name], Age: [age]" to a file called user_info.txt
Reads back the entire content and prints it """
import csv
with open("user_info.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=['name','age'])
    name = input("Enter your name: ")     
    age = int(input("Enter your age: "))
    writer.writerow({"name": name, "age": age})