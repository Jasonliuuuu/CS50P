class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        
    def start_engine(self):
        print(f"The {self.make} {self.model} engine is starting")
        

# Creating two instances (objects) of the Car class
car1 = Car("Ford", "Mustang", 1969)
car2 = Car("Tesla", "Model S", 2019)

# Accessing attributes and calling methods of the object

print(f"Car 1 is a {car1.year} {car1.make} {car1.model}")
print(f"Car 2 is a {car2.year} {car2.make} {car2.model}")


car1.start_engine()        

# In this example, Car is a class that represents cars. car1 and car2 are objects (instances) of the Car class, each with its own set of attributes (make and model) and methods (start_engine). The objects represent specific cars with unique make and model attributes. They can perform the operation of starting their engines using the start_engine method.