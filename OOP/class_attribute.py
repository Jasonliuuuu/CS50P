# class allow you to invent your own data type


class Student:
    pass

def main():
    student = get_student()
    print(f"Hello, { student.name } from { student.house }!")
    
    
def get_student():
    student = Student()
    student.name = input("What is your name? ")
    student.house = input("What is your house? ")
    return student

# We just create two attributes for the class Student

if __name__ == "__main__":
    main()