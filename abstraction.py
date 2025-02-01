
from abc import ABC, abstractmethod 

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):
    def eat(self):
        return "Tiger Will hunt and Eat"

class Deer(Animal):
    def eat(self):
        return "Deer Will graze and Eat"
    
class Bear(Animal):
    def eat(self):
        return "Bear will both hunt and graze and Eat"

# animal = Animal() # Error
# print(animal.eat())

animal = Tiger()
print(animal.eat())

animal = Deer()
print(animal.eat())

animal = Bear()
print(animal.eat())
