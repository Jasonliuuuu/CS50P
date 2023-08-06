class Student:
    def __init__(self, name = None, house = None):
        if not name:
            raise Exception("You must provide a name.")
        self.name = name
        self.house = house
    # self give you access to current object that you just created
    
    def __str__(self):
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def house(self):
        return self._house
    
    # Setter
    @house.setter
    def house(self, house):
        if house not in ("Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"):
            raise Exception("Not a valid house.")
        self._house = house


# Why do python know to call the getter and setter?
#because when you call student.hosue. while house is the name of getter or setter. And then it will jump to setter and not going to access that attribute directly. I am going to use the setter to set the value of the attribute. Because equal sign mean to set.

def main():
    student = get_student()
    # student.house = "Number 4 Privet Drive"
    # In order to access attriuute,
    # you need to use property decorator (getter) and setter decorator
    print(student)
    
def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return Student(name, house)

if __name__ == "__main__":
    main()