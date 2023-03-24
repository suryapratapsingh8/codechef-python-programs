# cook your dish here
t=int(input())
while t!=0:
    n=int(input())
    d=dict()
    for r in range(0,n):
        l=list(map(int,input().split()))
        for p in range(0,n):
            d[l[p]]=r,p
    s=0
    i,j=d[1]
    for k in range(1,n*n):
        p,q=d[k+1]
        s+=abs(p-i)+abs(q-j)
        i,j=p,q 
    print(s)
    t-=1
        