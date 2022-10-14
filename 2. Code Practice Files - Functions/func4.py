# 9. Arbitrary arguments - *args (Function accepts undefined number of arguments)
def user_info(*args):
    print(args) #prints tuple
    print("My country is " + user_info[2]) # fetch the item at index 2

user_info("Jane", 19, "Kenya")

# OR

def user_info(*details): # Can use another variable name other than args - Same result
    print(details) #prints tuple
    print("My country is " + user_info[2]) # fetch the item at index 2

user_info("Jane", 19, "Kenya")


# 10. Keyword arguments: key = value
def my_function(child3, child2, child1): #The order in which the keys are defined does not matter - child1,child2,child3 / child3,child2,child1
  print("The youngest child is " + child3) #Because the value will be mapped to the key called
  print("The eldest child is " + child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")


# 11. Arbitrary Keyword Arguments - **kwargs (in Dictionaries) 
def user_info(**kwargs):
    print(kwargs) #prints dictionary
    print("My country is " + user_info["country"]) # fetch the value at the key = country

user_info(name = "Jane", age = 19, country = "Kenya") 

# OR

def user_info(**details): # Can use another variable name other than kwargs - Same result
    print(details) #prints dictionary
    print("My country is " + user_info["country"]) # fetch the value at the key = country

user_info(name = "Jane", age = 19, country = "Kenya") 


# 12. Anonymous functions 
double = lambda x: x*2

print(double(5))
