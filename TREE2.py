# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    if l[0]==0:
        print(len(set(l))-1)
    else:
        print(len(set(l)))
        