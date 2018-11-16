import math
 
class Circle:
 
    def __init__(self, radius):
        self.__radius = radius
 
    def setRadius(self, radius):
        self.__radius = radius
 
    def getRadius(self):
        return self.__radius
 
    def __add__(self, another_circle):
        another_circle.__radius = another_circle.__radius[::-1]
        return Circle( self.__radius +  another_circle.__radius )
 
c1 = Circle('4')
print(c1.getRadius())
 
c2 = Circle('45')
print(c2.getRadius())
 
c3 = c1 + c2 # This became possible because we have overloaded + operator by adding a    method named __add__
print(c3.getRadius())
