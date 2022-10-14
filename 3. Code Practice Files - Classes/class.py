# Class - Has Properties and Methods(activities)
class Student:
    def __init__(self, n, c): #First method/ Constructor - for defining properties of class
        self.name = n         #self parameter   
        self.course = c       #pass other parameters to the method 

    def career(self):
        if self.course == "Python":
            print(self.name, "wants to be a developer.")
        elif self.course == "Business Management":
            print(self.name, "is an entrepreneur.")

    def study(self):
        print(self.name, "loves to study.")

#Object 1 - Instantiation of a class
john = Student("John Doe", "Python")
john.career()
john.study()

#object 2
student2= Student("Jane Marie", "Business Management")
student2.career()
student2.study()