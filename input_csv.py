import csv

name = input("WHat is your name? ")
home = input("Where is your home? ")

with open("students.csv", "a", newline = "") as file:
    writer = csv.DictWriter(file, fieldnames = ["name", "home"])
    writer.writerow({"name": name, "home": home})
   
 
# () is tuple, [] is list, {} is dictionary