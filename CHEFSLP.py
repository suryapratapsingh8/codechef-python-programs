# cook your dish here
for _ in range(int(input())):
    n,l,x=map(int,input().split())
    k=n-l
    print(min(k,l)*x)