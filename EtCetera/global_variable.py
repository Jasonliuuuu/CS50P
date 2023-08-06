balance = 0

def main():
    print("Balance is", balance)
    deposit(100)
    withfraw(50)
    print("Balance is", balance)
    
def deposit(amount):
    global balance
    balance  = balance + amount
    
def withfraw(amount):
    global balance 
    balance = balance - amount 
    
if __name__ == "__main__":
    main()