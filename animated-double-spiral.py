# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 21:17:23 2020

@author: iampj
"""
from subprocess import call
from time import sleep
import numpy as np
n = 19

def display(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i,j],end='')
        print()

def image(x,y):
    k = (n-1)//2
    return (k+(k-x),k+(k-y))


mat = [[" "]*(n+2)]*(n+2)
mat = np.array(mat)

i,j = (n-1)//2,(n-1)//2
mat[i,j] = "#"
x = 1
m = -1
rowWise = True
c = 1
flag = False
while i in range(n) and j in range(n):
    #print(f"{x}:{rowWise}:{m}")
    for l in range(x):
        if rowWise:
            if j+m in range(n):
                j+=m
            else:
                flag = True
                break
        else:
            if i+m in range(n):
                i+=m
            else:
                flag = True
                break
        mat[i,j] = "#"
        k,h = image(i,j)
        mat[k,h] = "#"
        sleep(0.1)
        call('clear',shell=True)
        display(mat)
    if flag:
        break
    if c == 1:    
        x+=1
    else:
        x+=2
    if c%2==0:
        m*=-1
    c+=1
    rowWise = not rowWise
    if c==200:
        break
input()
#  1  2  4  6  8...
#  -  -  +  +  -...
#  R  C  R  C  R...
#  
#  
#  
#  
