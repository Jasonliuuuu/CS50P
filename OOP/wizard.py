class Wizzard:
    def __init__(self, name):
        if not name :
            raise ValueError("Name is required")
        self.name = name
        
                

class Student(Wizzard):
    def __init__(self, name, house):
        super().__init__(name)
        self.age = house
        
        
class Professor(Wizzard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
wizard = Wizzard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Snape", "Potions")

        
