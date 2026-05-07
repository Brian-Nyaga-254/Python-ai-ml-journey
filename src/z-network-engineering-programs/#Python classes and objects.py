#Python classes and objects
from math import pi, pow
class Cylinder:
    def _init_(self, radius, height):
         self.radius = radius
         self.height = height

    def area(self) :
            S_A = ( pi * pow(self.radius,2)) + ( pi* self.radius**2*self.height)
            return S_A
    def volume(self):
            vol = pi*self.radius**2*self.height
            return vol

    cylinder = self.Cylinder(10,15)
    area = cylinder.area()
    volume = cylinder.volume()
    print("Area is ", area)
    print("Volume is ", volume)
        