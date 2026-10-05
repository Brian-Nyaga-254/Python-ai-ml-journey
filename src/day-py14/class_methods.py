import random

class Hat:
    houses = ["Embu","Kenya","Africa"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")