students = [
    {"name":"Brian", "house":"Embu"},
    {"name":"Frank", "house":"Kenya"},
    {"name":"Mugai", "house":"Africa"},
    {"name":"Maina", "house":"Embu"},
    {"name":"Jane", "house":"Embu"},
    
]
houses = set()
for student in students:
    houses.add(student["house"])
    """ if student["house"] not in houses:
        houses.append(student["house"]) """

for house in sorted(houses):
    print(house)