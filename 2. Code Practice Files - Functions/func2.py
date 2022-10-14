# 5. with more than one argument
def user_info(name, age, country):  #local variables
    print("Your name is " + name + " and you are " + age + " years old.")
    print("You live in " + country)

user_info("Jane", "19", "Luxembourg")

# print(name) #Will this be printed? NO. Because name is a local variable, can only be used within the function definition

# user_info("Jane", 19) #What happens when you leave one parameter out? ERROR. A function must receive all required arguments.


# 6. Default parameter value
# To solve the error above, you can have a default parameter value predefined for this; country = "Kenya"
def user_info(name, age, country = "Kenya"):  #local variables
    print("Your name is " + name + " and you are " + str(age) + " years old.")
    print("You live in " + country)

user_info("Jane", 19) #Picks default value for country when unspecified
user_info("Jane", 19, "Tanzania")


# 7. Prompt user for this information instead
# global variables
user_name = input("\nWhat is your name: ")
user_age = input("What is your age: ")
user_country = input("Which country do you live in: ")

user_info(user_name, user_age, user_country)

print(user_age) #Will this be printed? YES. user_age is a global variable
print(type(user_age)) # int/float or string? string - input() gets a string