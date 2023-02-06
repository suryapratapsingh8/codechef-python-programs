# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=l.count(0)
    c=0
    for i in range(n):
        if l[i]==0:
            c=i
            break 
        else:
            c=n
            
    g=(n-c)*100
    print(g+k*1000)
    
        