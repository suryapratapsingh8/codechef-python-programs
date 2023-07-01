# cook your di
t=int(input());
for i in range(1,t+1):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    f=0
    for i in a:
        if i+k-1>m:
            f=1 
            break
    if f==0:
        print("YES")
    else:print("NO")
    
    