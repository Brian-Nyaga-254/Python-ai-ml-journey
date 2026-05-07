students = [
    {'name': 'Brian', 'Location': 'Embu', 'Course': 'BSE'},
    {'name': 'Mugai', 'Location': 'Kenya', 'Course': 'BBIT'},
    {'name': 'Nyaga', 'Location': 'Africa', 'Course': 'BCIT'},

]

for student in students:
    print(student['name'], student['Location'] , student['Course'], sep = ':')