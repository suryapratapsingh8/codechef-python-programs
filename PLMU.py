import math
t=int(input())
for i in range(t):
    n=input()
    l=list(map(int,input().split()))
    zero=l.count(0)
    two=l.count(2)
    a=math.comb(zero,2)
    b=math.comb(two,2)
    print(a+b)