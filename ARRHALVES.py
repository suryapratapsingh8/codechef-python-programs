for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    o,c=0,0
    for j in range(len(l)):
        if l[j]<=n:
            c+=j-o
            o+=1
    print(c)