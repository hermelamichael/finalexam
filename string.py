'''
s1 = "Apple"
s2 = "ApplE"

print (s1 > s2) #lower case is greater than upper case #if it has more letters...
'''

def dec2bin(value):
    binNumber = ""
    while (value > 0):
        bit = value % 2
        binNumber = binNumber + str(bit)
        value = value // 2
    binNumber = binNumber[::-1]
    return binNumber

result = dec2bin(14)
print(result)