# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=0
    for i in range(n):
        n,a,b=map(int,input().split())
        y=n+n*b/100
        z=y-y*b/100
        l=l+a*(n-z)
    print(l)
        