import re

name = input("What is your name? " ).strip()
""" if "," in name:
    
    ? means space is either there or not"""
 
"""last, first = name.split(", ?")
    name = f"{first} {last}"
print(f"hello, {name}") """


"""(.+) groups first and last name"""
matches = re.search(r"^(.+), *(.+)$",name)
if matches:
    """ last, first = matches.groups()
    name = f"{first} {last}" """
    
    """  last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}" """
    
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

"""
:= operator allows you to assign a value from right to left and ask a boolean question

 if matches := re.search(r"^(.+), *(.+)$",name):
        name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}") """