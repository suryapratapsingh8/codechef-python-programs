# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    f=0
    for i in range(n):
        if l[i]<=f:
            f=f+1 
        else:
            break 
    print(f)
