# Parent class
class Mammal:
    def walk(self):
        print("Walk")
    def sleep(self):
        print("Sleep")
    def eat(self):
        print("Eat")

class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def meow(self):
        print("Meow")


dog1 = Dog()
dog1.walk()
dog1.bark()
dog1.sleep()
dog1.eat()
cat1 = Cat()
cat1.walk()
cat1.meow()
cat1.sleep()
cat1.eat()





