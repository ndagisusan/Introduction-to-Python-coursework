# Classes that inherit from more than one class
# For Code Reusability to inherit properties and methods from other classes 
class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

class Child(Father, Mother): #Added customization
    def sports(self):
        self.gardening()
        self.cooking()
        print("I enjoy sports")

c = Child()
# c.gardening()
# c.cooking()
c.sports()
