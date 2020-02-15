n = int(input("Enter n > "))
for i in range(1,2*n):
    for j in range(1,2*n):
        x = i if i<=n else 2*n-i
        y = j if j<=n else 2*n-j
        z = x if x<=y else y
        print(n+1-z,end='')
    print("\n",end='')
