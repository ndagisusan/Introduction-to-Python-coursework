# without a function
print("Happy birthday to you!" )
print("Happy birthday to you!" )
print("Happy birthday, dear Fred...")
print("Happy birthday to you!")


# With a function
def happy():
    print("Happy birthday to you!")

def singFred():
    happy()
    happy()
    print("Happy birthday, dear Fred...")
    happy()

singFred()


# Defining the name as an argument(arg)
def sing(person):
    happy()
    happy()
    print("Happy birthday, dear " + person + "...")
    happy()

sing("Fred")
sing("Jane")


# Get user input
name = input("What is your name: ")
sing(name) # Once

# In a loop
for i in range(3): # 3 times
    sing(name)
    print("\n")

