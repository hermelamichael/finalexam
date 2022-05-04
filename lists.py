'''
A = [4, 6, 1, 4]
print(A.sort()) # why is it not prining
'''

'''
A = [4, 6, 1, 4]
print(A[0:2]) #use slices to get values 
'''

'''
A = [[1,2,3],[4,5,6]] # array of 2d list 
#print(A[0])
print(A[1])
print(A[1][1])
'''

def readMatrix(matrix, nrows, ncols):
    print(matrix)
    for i in range(nrows):
        row = []
        for j in range(ncols):
            print("Matrix[",i,"][",j,"] = ", sep= "", end="") #
            value = int(input(""))
            row.append(value) #matrix is a list of lists # #(len) of lists says rows and columns is len of list within list 
        matrix.append(row)


def printMatrix(matrix):
    nrows = len(matrix)
    ncols = len(matrix[0])
    for i in range(nrows):
        for j in range(ncols):
            print(matrix[i][j]," ", sep="",end="")
        print()


#main program 

A = []
readMatrix (A,2,2)
printMatrix(A)