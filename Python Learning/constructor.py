""" 
default constructor


class Car:
    def __init__(self, brand, color): #default const.
        self.brand=brand
        self.color=color

car1=Car('Tesla','White') #values automatically set

print(car1.color,car1.brand)

"""

class Car:
    def __init__(self, brand, color):
        self.brand=brand
        self.color=color

car1=Car('Tesla','White') #values automatically set

print(car1.color,car1.brand)