import csv
info = []
with open("user_info.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        info.append(row)
for information in sorted(info, key=lambda information: information['name']):
    print(f"{information['name']} is {information['age']} old")