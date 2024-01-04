# Base Class
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, owner):
        super().__init__(name)
        self.owner = owner

    def bark(self):
        print(f"{self.name} barks!")


dog = Dog("Fido", "Justin")
dog.name
dog.bark()
print(dog.owner)
