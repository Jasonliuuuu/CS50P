# students = {
#     "Hermione": "Gryffindor",
#     "Draco": "Slytherin",
#     "Neville": "Gryffindor"
# }
# Dictionary

# # print(students["Hermione"])
# # print(students["Draco"])
# # print(students["Neville"])

# for student in students:
#     print(student, "is in", students[student])

students = [
    {"name": "Hermione", "house": "Gryffindor", "year": "1"},
    {"name": "Draco", "house": "Slytherin", "year": "2"},
    {"name": "Neville", "house": "Gryffindor", "year": "1"},
    {"name": "Fred", "house": "Slytherin", "year": None}
]

for student in students:
    print(student["name"], "is in", student["house"], "and was in", student["year"], "year")