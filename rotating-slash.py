from time import sleep
import subprocess as sp

a = [" # ",
     " # ",
     " # "]
b = ["  #",
     " # ",
     "#  "]
c = ["   ",
     "###",
     "   "]
d = ["#  ",
     " # ",
     "  #"]
frames = [a,b,c,d]
i = 0
c = 0
while True:
    if i==len(frames):
        i = 0
    sp.call('clear',shell=True)
    print("\n".join(frames[i]))
    i+=1
    c+=1
    sleep(0.1)
    if c>50:
        break
