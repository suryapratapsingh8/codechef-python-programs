t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    l1=set(range(a,b+1))
    l2=set(range(c,d+1))
    l=l1.union(l2)
    print(len(l))