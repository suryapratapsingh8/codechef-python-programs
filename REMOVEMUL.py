# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    s=(n*(n+1))//2
    k=sum(l)
    print(s-k)