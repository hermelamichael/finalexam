'''
fh = open("input.txt")
for line in fh:
    if line[-1] == '\n':
        line = line[:-1]
    sequence = line.split(" ")
    for i in range(len(sequence)):
        sequence[i] = int(sequence[i])
    print(sequence)
fh.close()
'''


'''
a = 10 
a += 10  # a = a + 10 
print(a)
'''
'''
value = int(input("Enter the value: "))
print(value)
'''

done = False 
while done == False: 
    try: 
        myinteger = int(input("Enter an integer Number: "))
        done = True 
    except Exception as ex:
        print("Incorrect input")
print("The integer value is: ", myinteger)