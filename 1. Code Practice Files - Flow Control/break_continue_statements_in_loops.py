##LOOPS - Same result for both loops
#For loop
for i in range(10):
    print(i)
print("\n")  #Prints a new line

#While loop
count = 0
while count < 10:
    print(count)
    count += 1
print("\n")  #Prints a new line


##BREAK - Same result for both loops
#For loop
for i in range(10):
    if i == 6:
        break
    print(i)
print("\n")  #Prints a new line

#While loop
i = 0
while i < 10:    
    if i == 6:
        break    
    print(i)
    i+=1
print("\n")  #Prints a new line


##CONTINUE - Same result for both loops
#For loop
for i in range(10):
    if i == 6:
        print("Skipped in continue")
        continue
    print(i)
print("\n")  #Prints a new line

#While loop
i = 0
while i < 10:    
    if i == 6: 
        print("Skipped in continue")
        i+=1 #Have to increment before continue
        continue    
    print(i)
    i+=1


