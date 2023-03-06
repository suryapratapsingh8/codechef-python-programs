# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    
    s=0
    for i in range(n):
        if s+l[i]<x:
            
            s=s+l[i]
        else:
            print(i+1)
            break 
    else:
        print(-1)