# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=max(l)
    y=min(l)
    c=k
    for i in l:
        if i>y:
            c=i
            break 
    else:
        c=y   
    print(abs(k-y)+abs(k-c)+abs(y-c))
        
        
            