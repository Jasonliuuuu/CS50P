# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Luna", "house": "Ravenclaw"},
#     {"name": "Draco", "house": "Slytherin"},
#     {"name": "Cedric", "house": "Hufflepuff"},
# ]

# house = []
# for student in students:
#     if student["house"] not in house:
#         house.append(student["house"])    
        
# for house in sorted(house):
#     print(house)
#--------------------------------------------------------------
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Luna", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Cedric", "house": "Hufflepuff"},
]

house = set()
print(type(house))

for student in students:
    house.add(student["house"])
        
for house in sorted(house):
    print(house)