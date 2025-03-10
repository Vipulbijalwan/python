"""
1- class and object 
2- polymorphism
3- encapsulation
4- inheritance
5- abstraction

uses of oops
1- code duplication
2- data hidding
3- reusbality
4- easy maintainance
"""
"""
class car():
    def start(self):
        print("Car is starting......")

    def stop(self):
        print("Car is stoping.......")


car1=car() # objects of car class
car2=car() # objects of car class

car1.start() #calling start method
"""


class Car:
    def set_details(self,brand,color):
        self.brand=brand
        self.color =color

    def show_details(self):
        print(f'This car is a {self.color} {self.brand}')

car1=Car()
car1.set_details("BMW",'RED')


car2=Car()
car2.set_details("BW",'GREEN')

car1.show_details()
car2.show_details()