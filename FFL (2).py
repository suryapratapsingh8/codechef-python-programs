# cook your dish here
for _ in range(int(input())):
    n,s=map(int,input().split())
    p=list(map(int,input().split()))
    k=list(map(int,input().split())) 
    f=100
    d=100
    for i in range (n):
        if k[i]==0:
            if p[i]<d:
                d=p[i]
        else:
            if p[i]<f:
                f=p[i]
    if s+d+f<=100:
        print('yes')
    else:
        print('no')