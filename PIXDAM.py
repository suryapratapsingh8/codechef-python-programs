# cook your dish here
import math
for _ in range(int(input())):
    h,w,x,y,k=map(int,input().split())
    a=h-y
    b=w-x
    p=a*a+b*b 
    d=math.sqrt(p)
    if d<k:
        print(1)
    else:
        print(0)
    
    
