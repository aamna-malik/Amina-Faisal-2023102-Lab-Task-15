class Bird:
    def move(self):
        return "Flies in the sky"

class Mammal:
    def move(self):
        return "Walks on land"

# Child class inheriting from both Bird and Mammal
class Bat(Bird, Mammal):
    def move(self):
        # Override move method from Bird
        bird_move = super(Bird, self).move()
        
        # Override move method from Mammal
        mammal_move = super(Mammal, self).move()

        # Combine both movements for a bat
        return f"A bat {bird_move} and {mammal_move}"

# Create an instance of the Bat class
bat = Bat()

# Call the overridden move method
print(bat.move())
