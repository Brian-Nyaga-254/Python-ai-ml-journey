"""
A program that asks user for 
monthly salary(decimal)
tax rate in percentage(whole number)
computes tax amount and net salary
displays both values with commas and 2 decimal places
"""
monthly_salary = float(input("Enter your monthly salary: "))
tax_rate = int(input("Enter the tax rate(percentage): "))
tax_amount = (tax_rate/100)* monthly_salary
net_salary = monthly_salary - tax_amount
print(f"Tax amount: {tax_amount: ,.2f}")
print(f"Net salary: {net_salary: ,.2f}")
