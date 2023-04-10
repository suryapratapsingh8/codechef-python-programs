# cook your dish here
for _ in range(int(input())):
    a,b=map(int,input().split())
    c=list(map(int,input().split()))
    d=a*b-sum(c)
    if d>0:
        print(d)
    else:
        print(0)
    