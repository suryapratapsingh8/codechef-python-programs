for  _ in range(int(input())):
    n,q=map(int,input().split())
    t=0
    s=0
    for i in range(q):
        a,b=map(int,input().split())
        t=t+abs(s-a)+abs(a-b)
        s=b 
    print(t)
    
