import re


# re.search(pattern, string, flags=0)

email = input("What is your email address?: ").strip()
# if re.search(r"^[^@]+@[^@]+.\.edu$", email):
#     print("Valid")
    
# # + means one or more to the left
# else:
#     print("Invalid")

# if re.search(r"^[a-zA-Z0-9]+@[a-zA-Z0-9]+.[a-zA-Z0-9]+$", email):
#     print("Valid")
# else:
#     print("Invalid")
    
if re.search(r"\w+@\w+\.\w+", email):
    print("Valid")
else:
    print("Invalid")
    
# \d = [0-9]
# \D = [^0-9]
# \w = [a-zA-Z0-9_] 
# \W = [^a-zA-Z0-9_]
# \s = whitespace
# \S = non-whitespace

# flag = INGORECASE it means that it will ignore the case of the letters
# flag = MULTILINE it means that it will ignore the newline character
# flag = DOTALL it means that it will ignore the newline character
