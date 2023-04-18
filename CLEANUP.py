for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l2=[]
    for i in range(1,n+1):
        if i not in l:
            l2.append(i)
    ep=[]
    op=[]
    for i in range(0,len(l2)):
        if i%2==0:
            ep.append(l2[i])
        else:
            op.append(l2[i])
            
    if len(ep)==0:
        print("-1")
    else:
        print(*ep)

    if len(op)==0:
        print("-1")
    else:
        print(*op)