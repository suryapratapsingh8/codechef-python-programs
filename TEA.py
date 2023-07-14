# cook your dish here
import math
t=int(input())
for i in range(t):
        x,y,z=map(int,input().split())
        if y>=x:
                print(z)
        elif y<x:
                print(math.ceil(x/y)*z)
              
                
        