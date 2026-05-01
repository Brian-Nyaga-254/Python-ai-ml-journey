"""
Ask the user for their full name
Clean the input:
Remove leading/trailing spaces
Format the name:
Capitalize it properly
Ask the user how they are feeling today (one word)
"""
name = input('What is your name: ')
name = name.strip()
name = name.capitalize()
mood = input("How are you feeling today: ")
mood = mood.strip()
mood = mood.capitalize()
print(f"Hello {name} I see you are feeling {mood} today")


