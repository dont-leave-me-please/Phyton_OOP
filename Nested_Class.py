

class Student:

    class Address:

        def __init__(self, city, country):
            self.city = city
            self.country = country

        def show_address(self):
            print(f"{self.city}, {self.country}")


address = Student.Address("Tokyo", "Japan")

address.show_address()

class Car:

    class Engine:
        def start(self):
            print("Engine is starting")


engine = Car.Engine()

engine.start()

class Car:

    def __init__(self, brand):
        self.brand = brand

    class Engine:

        def start(self):
            print("Engine starts")

car = Car("Toyota")

engine = Car.Engine()

engine.start()