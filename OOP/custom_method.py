class Student:
    def __init__(self, name = None, house = None, patronus = None):
        if not name:
            raise Exception("You must provide a name.")
        self.name = name
        self.house = house
        self.patronus = patronus
    # self give you access to current object that you just created
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return ("horse")
            case "Otter":
                return ("cool")
            case "Jack Russell Terrier":
                return ("dog")
            case _:
                return ("unknown")

def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())
    
def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    patronus = input("What is your patronus? ") 
    return Student(name, house, patronus)

if __name__ == "__main__":
    main()