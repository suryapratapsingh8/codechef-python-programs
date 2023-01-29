# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    k=(n*(n+1)//2)*(m*(m+1)//2)
    print(k-m*n)