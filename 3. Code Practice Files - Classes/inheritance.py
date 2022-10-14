# Classes that inherit from one main class
# eg. Car and motorcycle classes inherit from Vehicle class
# eg. Student and Worker classes inherit from Human class

class Vehicle: #Base/Parent class
    def general_usage(self):
        print("General use: Transportation.")

class Car(Vehicle): # Derived class...Inheritance - Car inherits from Vehicle
    def __init__(self):
        print("Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        print("Specific use: Commute to work, vacation with family")

class Motorcycle(Vehicle): # Derived class...Inheritance - Motorcycle inherits from Vehicle
    def __init__(self):
        print("Motorcycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage() # Call the general_usage method in the parent class within the derivative class
        print("Specific use: Offroading, Racing")

#Object 1
c = Car()
c.general_usage() #Inherited method (from the Parent Class) which is not defined in the Car class 
c.specific_usage()

# #Object 2
m = Motorcycle()
# m.general_usage() #Inherited method (from the Parent Class) which is not defined in the Car class 
m.specific_usage()

# The general_usage method can also be called within the class
# Output the same result

#isinstance and issubclass methods - Built-in Python functions
# isinstance - Checks if an object is an instance of a class 
print(isinstance(c,Car))
#What is the expected output?

# issubclass - Checks if a class is a subclass of another class
print(issubclass(Motorcycle,Car)) #What is the expected output?

