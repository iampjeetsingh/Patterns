import numpy as np

n = int(input("Enter n > "))
n = 5+4*(n-1)
s = "#"
mat = [[" "]*n]*n
mat = np.array(mat)



def printMat(mat):
    for row in range(n):
        for column in range(n):
            print(mat[row,column],end='')
        print()





i,j = n//2,n//2
mat[i,j] = s

c = 0
m = 1
x = 2
colOperation = True
stop = False
while i in range(n) and j in range(n):
    for step in range(x):
        if colOperation:
            if i+m in range(n):
                i += m
            else:
                stop = True
                break
        else:
            if j+m in range(n):
                j += m
            else:
                stop = True
                break
        if stop:
            break
        mat[i,j] = s
    colOperation = not colOperation
    c += 1
    if c==2:
        x+=2
        c=0
    elif c==1:
        m*=-1
printMat(mat)

# 2 2 4 4 6 6 8 8
# + - - + + - - +
# C R C R C R C
