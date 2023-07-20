# cook your dish here
for _ in range(int(input())):
    n,s=map(int,input().split())
    k=(n*(n+1))//2
    y=k-s
    if y>=1 and y<=n:
        print(y)
    else:
        print(-1)