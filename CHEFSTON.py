# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    m=0
    for i in range(n):
        c=k//a[i]
        d=b[i]*c 
        if d>m:
            m=d 
    print(m)