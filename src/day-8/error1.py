while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number > 0:
            break
        else:
            print("Number must be greater than zero.")
    except ValueError:
        print("Invalid value")

    count = 0

    for i in range(0, number + 1):
        if i % 2 == 0:
            print(i)
        count += 1

        print("Total even numbers: ", count)