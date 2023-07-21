for i in range(int(input())):
    n,k=map(int,input().split())
    p=list(map(int,input().split()))[:n]
    #print(p)
    l=[]
    for i in p:
        if(i>k):
            l.append(k)
        else:
            l.append(i)
    #print(l)
    print(sum(p)-sum(l))