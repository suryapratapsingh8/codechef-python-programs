# cook your dish here
import math
for _ in range(int(input())):
    a=int(input())
    if a<5:
        print("NO")
    else:
        x=0
        for i in range(1,int(math.sqrt(a))):
            b=(a-2*i)/(2+i)
            if b==int(b):
                print("Yes")
                x=1
                break
        if x==0:
            print("no")