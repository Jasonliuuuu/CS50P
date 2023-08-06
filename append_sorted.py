# names = []
# for _ in range(3):
#     name = input("  What is your name? ")
#     names.append(name)

# for name in sorted(names):
#     print(f"Hello, {name}!")
#--------------------------------------------------------------
# name = input("What's your name?")

# file = open("names.txt", "a")
# file.write(name + "\n")
# file.close()
#--------------------------------------------------------------

for x in range(3):
    name = input("What's your name?")

    with open("names.txt", "a") as file:
        file.write(f"{name}\n")
