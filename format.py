import re

name = input("Enter your name: ").strip()

matches  = re.search("^(.+), (.+)$", name)

if matches:
    name = matches.group(2) + " " + matches.group(1)
    
print(f"hello {name}!")