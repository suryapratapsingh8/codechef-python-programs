# cook your dish here
import math
for  _ in range (int(input())):
    n,a,b,c,d,e,f=map(int,input().split())
    k=math.ceil(n/2)
    y=a+b+c+d+e+f 
    print(y*k)
