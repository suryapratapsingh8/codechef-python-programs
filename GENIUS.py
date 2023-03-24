# cook your dish here
import math
t=int(input())
while(t):
    n,x=map(int,input().split())
    a=math.ceil(x/3)
    b=a*3-x
    c=n-a-b
    if(c>=0):
        print("YES")
        print(a,b,c) 
    else:
        print("NO")
    t-=1
