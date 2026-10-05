def meow(n: int) -> str:
    
    """
    Meow n times.

    :param n:Numbers of time to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A STRING OF N MEOWS, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")