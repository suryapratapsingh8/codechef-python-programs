import math
k=int(input())
for t in range(k):
    n=int(input())
    a=list(map(int, input().split()))
    ct=0
    if n==1:
        print(1)
    else:
        pr=[0]*n
        su=[0]*n
        pr[0]=a[0]
        su[n-1]=a[n-1]
        for i in range(1,n):
            pr[i]=math.gcd(pr[i-1],a[i])
        for i in range(n-2,-1,-1):
            su[i]=math.gcd(su[i+1],a[i])
        for i in range(n):
            if i==0:
                if su[i+1]!=1:
                    ct+=1
            elif i==n-1:
                if pr[i-1]!=1:
                    ct+=1
            elif math.gcd(su[i+1],pr[i-1])!=1:
                ct+=1
        print(ct)