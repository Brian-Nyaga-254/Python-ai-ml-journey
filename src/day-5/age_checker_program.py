"""
This program checks the age category of a user based on their input age.
Categories:
- Child: 0 - 12
- Teenager: 13 - 19
- Adult: 20 - 59
- Senior: 60 - 130
"""
def age_category(age):
    if age > 0 and age < 13:
        return "Child"
    elif age >= 13 and age <= 19:
        return "Teenager"
    elif age >= 20 and age <= 59:
        return ("Adult")
    elif age >= 60 and age <= 130:
        return "Senior"
    else:
        return "Invalid Age!"
    

def main():
        user_input = int(input("Enter your age: "))
        final_result = age_category(user_input)
        print(final_result)


main()        
    