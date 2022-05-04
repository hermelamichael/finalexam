'''
value = 10 
print(id(value))
value = 20
print(id(value))
'''

'''
value = "Carlos"
value[0] = 'M'
print(value)
#strings are immutable so you cant replace butttt....
'''

'''
value = "Carlos"
value = value.replace("C", 'M')
print(value) #id is different though which makes it immutable 
'''

value = "Carlos"
print(value)
for ch in range(len(value)):
    print(value[ch]) #python is going through each character 

