n = int(input("Enter n > "))

for x in range(1,2*n):
    for y in range(1,2*n):
        if (x+y)%2==0:
            print((x+y)//2,end='')
        else:
            print(" ",end='')
    print("\n",end='')
