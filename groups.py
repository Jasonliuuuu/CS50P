import re 

email = input("What is your email address?: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+$", email):
    print("Valid")
    
else:
    print("Invalid")
    
    
# if re.search(r"^\w+@\w+\.\w+$", email):
#     print("Valid")
    
# else:
#     print("Invalid")
    
# . means any character
# * means zero or more to the left
# ? means zero or one to the left

# ^ means start of line
# + means one or more to the left
# {m} means exactly m copies of the previous RE
# {m,n} means from m to n copies of the previous RE