class Animal():
    def __init__(self, name):
        self.name = name
        self.is_alive = True
    def eat(self):
        print(f"{self.name} is eating.")
    def sleep(self):
        print(f"{self.name} is sleeping.")
class Dog(Animal):
    pass
class Cat(Animal):
    pass
class Mouse(Animal):
    pass
dog = Dog("buddy")
cat = Cat("kitty")
mouse = Mouse("mickey")
dog.eat()
cat.eat()
mouse.eat()
dog.sleep()
cat.sleep()
mouse.sleep()