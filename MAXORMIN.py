# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    a=l.count(1)
    b=l.count(0)
    if a>=b:
        print(1)
    else:
        print(0)