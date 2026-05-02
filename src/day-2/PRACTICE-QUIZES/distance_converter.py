"""
A program that asks user for distance in kilometers
converts it into meters and centimeters
displays 
meters as an integer
centimeters with commas
"""
distance = float(input("Enter distance in kilometers: "))
meters =int(distance * 1000)
centimeters =int(distance * 1000000)
print(f"Meters: {meters}")
print(f"Centimeters: {centimeters:,}")
