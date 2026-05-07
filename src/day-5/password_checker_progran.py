"""
This program checks user credentials and grants or denies access based on the input username and password.
correct_username: "admin"
correct_password: 1234
"""
correct_username = "admin"
correct_password = 1234

username = input("Enter your username: ")
password = int(input("Enter your password: "))
if username == correct_username and password == correct_password:
    print("Access granted")
elif username == correct_username and password != correct_password :
    print("Wrong password")
else:
    print("Unknown user")

