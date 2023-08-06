class Vault:
    def __init__(self, galleos = 0, sickles = 0, knuts = 0):
        self.galleos = galleos
        self.sickles = sickles
        self.knuts = knuts
        
    def __str__(self):
        return f"Galleos: {self.galleos}, Sickles: {self.sickles}, Knuts: {self.knuts}"
    
    def __add__(self, other):
        galleos = self.galleos + other.galleos
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleos, sickles, knuts)
        
        
potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(potter)

total = potter + weasley
print(total)