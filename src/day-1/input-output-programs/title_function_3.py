#Ask user to input their name
name = input('What is your name? ').strip().title()
#Split users name into 3
first, second, third =name.split(" ")
#Greet the user with their name
print(f"Hello,{second} {third}" )

