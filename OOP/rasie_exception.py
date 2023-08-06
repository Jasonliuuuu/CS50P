class Student:
    def __init__(self, name = None, house = None):
        if not name:
            raise Exception("You must provide a name.")
        self.name = name
        self.house = house
    # self give you access to current object that you just created
    
    def __str__(self):
        return f"{self.name} from {self.house}"


def main():
    student = get_student()
    # print(f"Hello, { student.name } from { student.house }!")
    print(student)
    
def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return Student(name, house)

if __name__ == "__main__":
    main()