#how to print without the brackets 

myString = "10 20 30 40"
myList = myString.split() #split function that recieves a serperator 
 #trying to convert list into integers 
for value in myList:
    print(value, "",end="")
print()
print(myList)