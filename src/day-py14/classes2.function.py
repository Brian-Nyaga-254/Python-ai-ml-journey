class Car:
    ...
def main():
    car = get_car()
    print(f"{car.name} {car.year} {car.color} is the car you have chosen")

def get_car():
    car = Car()
    car.name = input("Enter car  name:" )
    car.year = int(input("Enter year car was made: "))
    car.color = input("Enter color you want: ")
    return car

if __name__ =="__main__":
    main()