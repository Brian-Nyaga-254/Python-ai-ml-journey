principle = float(input("Enter the principle: "))
rate = float(input("Enter the rate: "))
time = float(input("Enter the time: "))
simple_interest = principle *( rate)/100 * time
print(f"The simple interest is: {simple_interest:.2f}")