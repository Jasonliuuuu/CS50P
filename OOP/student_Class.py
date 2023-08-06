class Student:
    def __init__(self, name = None, house = None):
        self.name = name
        self.house = house
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    @classmethod
    def get(cls):
        name = input("What is your name? ")
        house = input("What is your house? ")
        return cls(name, house)
    
# cls is one of the feature of Object oriented programming. You can now instantiate a student object by using cls. 

def main():
    student = Student.get()
    print(student)
    
# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return Student(name, house)

if __name__ == "__main__":
    main()