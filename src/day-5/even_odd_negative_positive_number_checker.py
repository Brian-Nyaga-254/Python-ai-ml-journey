"""
This program classifies a number as even or odd and as positive, negative, or zero. 
Categories:
- Zero: 0
- Positive even: > 0 and divisible by 2
- Positive odd: > 0 and not divisible by 2
- Negative even: < 0 and divisible by 2
- Negative odd: < 0 and not divisible by 2
"""
def classify_number (n):    
    if n == 0:
        return "Zero"
    elif n > 0 and n % 2 == 0:
        return "Positive even"
    elif n > 0 and n % 2 != 0:
        return "Positive odd"
    elif n < 0 and n % 2 == 0:
        return "Negative even"
    else:
        return "Negative odd"


def main():
    number = int(input("Enter a number: "))
    result = classify_number (number)
    print(result)


main()







