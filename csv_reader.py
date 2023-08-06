import csv 

students = []

# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, home in reader:
#         students.append( { "name": name, "home": home } )
        
# for student in sorted(students, key = lambda student: student["name"]):
#     print(f"{ student['name'] } is from { student['home'] }")

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append( { "name": row["name"], "home": row["home"] } )

#Using DicrtReader, this is beneficial because it enables us to access the values in each row using their column names.

for student in sorted(students, key = lambda student: student["name"]):
    print(f"{ student['name'] } is from { student['home'] }")