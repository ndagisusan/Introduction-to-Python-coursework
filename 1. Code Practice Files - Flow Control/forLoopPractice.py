#For loop in lists
groceries = ['apples', 'bananas', 'tomatoes']

for item in groceries:
    print(item) #Prints the items
    print(item[3]) #Print the 4th letter in each item
print("\n")  #Prints a new line   

#For loop in intergers
for i in range(9):
    print(i) # 0 - 8
print("\n")

#For loop in intergers - start at 1, end at 4 (excudes 9)
for i in range(1, 9):
    print(i)
print("\n")

#For loop in intergers - start at 1, end at 9, in steps of 2 
#(Question: Will 9 be printed?)
for i in range(1, 9, 2):
    print(i)   

#Pass - placeholder for future code, ensures no errors
for i in range(10):
    pass 