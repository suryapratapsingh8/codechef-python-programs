import math
def is_prime(j):
    if j<=1:
        return False
    if j==2 or j==3:
        return True
    if j%2==0 or j%3==0:
        return False
    num=math.floor(math.sqrt(j))
    for k in range(5,num+1,6):
        if j%k==0 or j%(k+2)==0:
            return False
    return True
t=int(input())
for i in range(t):
    n,m=map(int,input().split())
    for j in range(n,m+1):
        res=is_prime(j)
        if res!=0:
            print(j)