import re
name = input("Enter your name: ")


"""
IF STATEMENT

 name = input("Enter your name: ")
if "," in name:
    last , first = name.split(",?")
    name = f"{first} {last}"
print(f"hello,{name}") """

"""RE.SEARCH"""

if matches := re.search(r"^(.*),(.*)$", name):
 
   """ matches:
       last , first = matches.groups()
    last = matches.group(1)
    first = matches.group(2) """
    
   name = matches.group(2) + " " + matches.group(1)
print(f"Hello, {name}")