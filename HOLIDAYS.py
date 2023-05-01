# cook your dish here
for _ in range(int(input())):
    n,w=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=0
    
    for i in range(n):
        if s>=w:
            break
        else:
            s=s+l[i]
            n=n-1
            
    print(n)
        