# cook your dish here
import math
for i in range(int(input())):
    a,b=map(int,input().split())
    count=0
    d=abs(a-b)
    r=math.sqrt(d)
    for i in range(1,int(r+1)):
        if d%i==0:
            count=count+1
            if d//i!=i:
                count=count+1
    print(count)
        