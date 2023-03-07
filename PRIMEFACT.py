# cook your dish here
import math
for _ in range(int(input())):
    x,y=map(int,input().split())
    for i in range(2,x+1):
        if x%i==0:
            x=x+i 
            break 
    k=math.ceil((y-x)/2)
    print(k+1)
        
