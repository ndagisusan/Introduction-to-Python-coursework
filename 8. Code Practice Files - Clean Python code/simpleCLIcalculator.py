print("\nWelcome to Simple CLI Calculator!\n") # CLI - Command Line Interface

isrunning = True # Not 'true'

# Show the usage of conditions and loops in the same program - Real world scenario
while isrunning:        # Loop (continue and break are also used in the loop)  
    print("Starting Calculator Process...\n")
    operation = input("Please enter the operation you would like to perform.\nPick one from these: [+, -, *, /, %]: ")
    
    try:        # Input Validation
        no1 = float(input("\nPlease enter a number: "))         # Number = float (int or otherwise)
        no2 = float(input("Please enter another number: "))

    except:
        print("Failed, invalid number!\n")      #\n - starts a new line
        continue        # Take us back to start of Loop until input validation check is passed
        
    if operation == "+":
        print(no1 + no2)
    elif operation == "-":
        print(no1 - no2)       
    elif operation == "*":
        print(no1 * no2)           
    elif operation == "/":
        print(no1 / no2)
    elif operation == "%":
        print(no1 % no2)
    else:
        print("Invalid operation, try again...")

    choice = input("\nDo you wanna try another calculation: [y,n]: ")
    if choice == "y":
        pass

    if choice == "n":
        isrunning = False # Or break - This ends the loop

print("\nThanks for using the calculator. Bye bye!\n")

# Question: How can you make this program better using fewer lines of code?
    # Using functions
    # Lists can be used to make use of many operations at once