class Account:
    def __init__(self):
        self._balance = 0
    
    # Getter
    @property    
    def balance(self):
        return self._balance
    
    
    def deposit(self, amount):
        self._balance = self._balance + amount
        
    def withdraw(self, amount):
        self._balance = self._balance - amount
        
        
def main():
    account = Account()
    print("Balance is", account.balance)
    # account.balance = 1000000
    # we can not execute this because we do not have setter, in this case, we only use getter since they we only want to access the value of the attribute
    account.deposit(100)
    account.withdraw(50)
    print("Balance is", account.balance)
    
if __name__ == "__main__":
    main()