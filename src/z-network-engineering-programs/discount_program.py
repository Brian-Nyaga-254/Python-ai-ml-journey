amount = float(input("Enter the total amount: "))
if amount >= 5000:
    discount = amount * (10/100)
elif amount >= 1000 and amount <= 4999:
    discount = amount * (5/100)
else:
    print("No discount")

print(f"Your discount is: {discount}")