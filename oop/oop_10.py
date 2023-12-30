class Cat:
    def sound(self):
        return "Meow"

class Dog:
    def sound(self):
        return "Woof"

def make_sound(animal):
    return animal.sound()

my_cat = Cat()
my_dog = Dog()
print(make_sound(my_cat))
print(make_sound(my_dog))
