import math 
t=int(input())
for i in range(t):
    n,a,b,k=map(int,input().split())
    if (n//a+n//b)-(n//math.lcm(a,b))*2>=k:
        print('Win')
    else:
        print('Lose')