# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    for i in range(k):
        if l[i]<0:
            l[i]=l[i]*-1
        else:
            break 
    s=0
    for i in (l):
        if i>0:
            s=s+i 
    print(s)
        