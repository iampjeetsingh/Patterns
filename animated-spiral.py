import numpy as np
import subprocess as sp
from time import sleep
from colorama import Fore, Back, Style

n = 10
n = 5+4*(n-1)
s = "#"
mat = [[" "]*n]*n
mat = np.array(mat)

path = []
colors = [Fore.RED,Fore.GREEN,Fore.BLUE]

def printMat(mat,color):
    for row in range(n):
        for column in range(n):
            print(color + mat[row,column],end='')
        print()

i,j = n//2,n//2
mat[i,j] = s
path.append((i,j))

c = 0
m = 1
x = 2
rowOp = True
stop = False
while i in range(n) and j in range(n):
    for step in range(x):
        if rowOp:
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
        mat[i,j] = s
        path.append((i,j))
    if stop:
            break
    rowOp = not rowOp
    c += 1
    if c==2:
        x+=2
        c=0
    elif c==1:
        m*=-1
        

i = 0
c = 0
mat = [[" "]*n]*n
mat = np.array(mat)
j = 0
while True:
    mat[path[i][0],path[i][1]] = s
    sp.call('clear',shell=True)
    printMat(mat,colors[j])
    i+=1
    c+=1
    j+=1
    if j==len(colors):
        j=0
    if i==len(path):
        break
    sleep(0.1)

# 2 2 4 4 6 6 8 8
# + - - + + - - +
# C R C R C R C
