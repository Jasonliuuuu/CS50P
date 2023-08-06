# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{ row[0] } is in { row[1] }")
#----------------------------------------------------------
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{ name } is in { house }")

#----------------------------------------------------------
# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{ name } is in { house }")


# for student in sorted(students):
#     print(student)
    
# ----------------------------------------------------------
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
        
# for student in students:
#     print(f"{ student['name'] } is in { student['house'] }")
    
    
# ----------------------------------------------------------
# students = []
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house} 
#         students.append(student)
        
# def get_name(student):
#     return student["name"]

# def get_house(student): 
#     return student["house"]
        
# for student in sorted(students, key= get_name):
#     print(f"{ student['name'] } is in { student['house'] }")

#----------------------------------------------------------
students = []
with open("students.csv") as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {"name": name, "home": home} 
        students.append(student)
        
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{ student['name'] } is from { student['home'] }")
    
#it turns out if we have multile "," in the csv, they may show too many value to upack
# so we introduce the csv module to handle this problem