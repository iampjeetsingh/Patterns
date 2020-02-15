n = int(input("Enter n > "))

for i in range(1,2*n):
    x = i if i<=n else 2*n-i 
    spaces = " "*(2*x-2)
    hashes = "#"*(n+1-x)
    print(spaces+hashes)
