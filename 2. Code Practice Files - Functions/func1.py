#def keyword

# 1. With no arg
def new_func(): #function definition
    print ("Hello\n")

new_func()  #Function call


# 2. Func with an arg
def fn(x):    
    print (x*3)

fn(5)

# OR
def func(x):
    return x*3

print(func(5))


# 3. Get user input eg. mailmerge
def get_input():
    user_input = input("\nWhat is your name? ")
    print("Dear " + user_input +"\n")
    
get_input()


# 4. With a loop
def country():
    name = input("Country please: ")
    print("Happy to be here.\n")

#for loop
# for i in range(3): #calls the function 3 times
#     country()

# while loop
i = 0
while i < 3:
    country()
    i = i + 1 #i += 1

# Ctrl + / to comment and uncomment in VS Code