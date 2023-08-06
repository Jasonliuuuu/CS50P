import random

class Hat:
    
    house = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
        
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.house)
        print(f"{name} goes to {house}")


Hat.sort("Harry")