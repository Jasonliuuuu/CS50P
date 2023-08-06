# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#     # self give you access to current object that you just created


# def main():
#     student = get_student()
#     print(f"Hello, { student.name } from { student.house }!")
    
    
# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     student = Student(name, house)
#     return student

# if __name__ == "__main__":
#     main()
    
# instance method is a method that is bound to an instance of a class

class Student:
    def __init__(self, name = None, house = None):
        self.name = name
        self.house = house
    # self give you access to current object that you just created


def main():
    student = get_student()
    print(f"Hello, { student.name } from { student.house }!")
    
    
def get_student():
    student = Student()
    student.name = input("What is your name? ")
    student.house = input("What is your house? ")
    return student

if __name__ == "__main__":
    main()