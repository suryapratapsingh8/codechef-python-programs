# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    c=0
    for i in (l):
        if i>=x:
            c=c+1 
    print(c)