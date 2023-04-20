import math
for i in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    x=math.gcd(l[0],l[1])
    for i in range(1,a):
        x=math.gcd(l[i],x)
        if x==1:
            break
    print(x*a)