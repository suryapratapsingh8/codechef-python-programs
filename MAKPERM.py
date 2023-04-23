# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=set(l)
    
    c=0
    for i in (list(k)):
        if i<=n:        
            c=c+1  
    print(n-c)