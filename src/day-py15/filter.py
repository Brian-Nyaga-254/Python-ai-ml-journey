students = [
    {"name":"Brian", "house":"Embu"},
    {"name":"Frank", "house":"Kenya"},
    {"name":"Mugai", "house":"Africa"},
    {"name":"Maina", "house":"Embu"},
    {"name":"Jane", "house":"Embu"},
    
]
def is_embu(s):
    return s["house"] == "Embu"

embus = filter(is_embu, students)

for embu in sorted(embus, key=lambda s: s["name"]):
    print(embu["name"])