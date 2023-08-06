def main():
    x = get_int("what is y? ")
    print(f"x is {x}")
    
def get_int(promt):
    while True:
        try:
            return int(input(promt))
        except ValueError:
            pass
        
main()