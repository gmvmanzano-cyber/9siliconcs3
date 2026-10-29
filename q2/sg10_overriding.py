class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return "Animal eats food."
        #Used if function does nothing. This is so because it is only for getting overriden.
    def make_sound(self):
        return "Animal makes sound!"

class Lion(Animal):
    def __init__(self, name):
        super().__init__(name) 
        #Super function was used to get the self.name = name from parent class.

    def eat(self): #Overrid the parent function's eat with own.
        return f"{self.name} eats fresh meat."
    def make_sound(self):
        return f"{self.name} roars loudly!" #Overrid the parent function's make_sound with own.

class Elephant(Animal):
    def __init__(self, name):
        super().__init__(name) 

    def eat(self):
        return f"{self.name} eats grass and fruits."
    def make_sound(self):
        return f"{self.name} trumpets!"

class Monkey(Animal):
    def __init__(self, name):
        super().__init__(name) 

    def eat(self):
        return f"{self.name} eats bananas."
    def make_sound(self):
        return f"{self.name} chatters!"

lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

print(lion.make_sound())
print(lion.eat())
print("-----")

print(elephant.make_sound())
print(elephant.eat())
print("-----")

print(monkey.make_sound())
print(monkey.eat())
print("-----")