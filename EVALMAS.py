for i in range(int(input())):
    n,x=map(int,input().split())
    m=1
    s=""
    for i in range(n):
        if m<x:
            m+=1
            s+="+"
        elif m>x:
            m-=1
            s+="-"
        else:
            s+="*"
    if m==x:
        print(s)
    else:
        print(-1)