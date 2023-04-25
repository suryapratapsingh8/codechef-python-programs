# cook your dish here
import math
for i in range(int(input())):
    x,k=map(int,input().split())
    c=0
    while(x/k>0):
        x=math.floor(x/k)
        c+=1
    print(c)