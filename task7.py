class Animal:
    num_of_insts = 0

    def __init__(self):
        Animal.num_of_insts = Animal.num_of_insts + 1

    def print_num():
        print(Animal.num_of_insts)

    print_num = staticmethod(print_num)

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
Animal.print_num()