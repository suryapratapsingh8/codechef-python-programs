# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    y=min(n-k,k)
    l.sort()
    s=0
    for i in range(y):
        s=s+l[i]
    print(sum(l)-2*s)
    