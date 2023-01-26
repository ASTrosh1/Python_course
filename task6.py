class Animal:
    def voice(self):
        pass

class Dog(Animal):
    def voice(self):
        print("Woof")

class Cat(Animal):
    def voice(self):
        print("Meow")

class Cow(Animal):
    def voice(self):
        print("Mooo")

d = Dog()
c = Cat()
w = Cow()
d.voice()
c.voice()
w.voice()