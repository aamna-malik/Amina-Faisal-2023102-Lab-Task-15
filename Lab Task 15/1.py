from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
    
    @abstractmethod
    def move(self):
        pass

# Child class 1
class Lion(Animal):
    def speak(self):
        return "Roar"
    
    def move(self):
        return "Walks on four legs"

# Child class 2
class Snake(Animal):
    def speak(self):
        return "Hiss"
    
    def move(self):
        return "Slithers on the ground"

# Usage example
lion = Lion()
snake = Snake()

print("Lion says:", lion.speak())
print("Lion moves:", lion.move())

print("Snake says:", snake.speak())
print("Snake moves:", snake.move())
