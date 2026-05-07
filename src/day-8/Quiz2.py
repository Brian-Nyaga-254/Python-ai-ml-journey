"""
 A program that asks user for a password.
 User has 3 attempts to fill in the correct password
"""
password = "python123"
attempt = 0
max_attempts = 3

while attempt < max_attempts:
      user_input = input("Enter the password: ")
      if user_input == password:
            print("Access granted")
      else:
         attempt += 1      
         print(F"Wrong password.Attempts left: {max_attempts - attempt}")
else:
      print("Access denied")   
       


    
         