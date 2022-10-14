# Classes that inherit from more than one class
# For Code Reusability to inherit properties and methods from other classes 
class Father():
    def skills(self):
        print("gardening, plumbing")

class Mother():
    def skills(self):
        print("cooking, art")

class Child(Father, Mother): #Added customization
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports, programming")

c = Child()
c.skills()
