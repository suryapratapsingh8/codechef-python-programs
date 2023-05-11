import math
t=int(input())
for i in range(t):
    n,x=list(map(int,input().split()))
    
    if 2*x>=n:
        print('yes')
    else:
        print('no')