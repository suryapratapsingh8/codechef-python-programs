# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    c=0
    for i in range(k,n-k):
        c=c+l[i]
    d=n-2*k 
    print(c/d)
