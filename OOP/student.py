def main():
    student = get_student()
    if student["name"]  == "Padma":
        student["house"] = "Ravenclaw"
    print(f"Hello, { student['name'] } from { student['house'] }!")

# def get_student():
#     name = input("What is your name? ")
#     house = input("What is your house? ")
#     return [name, house]

# def get_student():
#     student = {}
#     student["name"] = input("What is your name? ")
#     student["house"] = input("What is your house? ")
#     return student
# we fon't need to create a dictionary and then add one key, and then second key to it, and then return it. We can just create an empty dictionary and then add keys to it as we go along.

def get_student():
    name = input("What is your name? ")
    house = input("What is your house? ")
    return { "name": name, "house": house }

if __name__ == "__main__":
    main()