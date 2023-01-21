# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=sum(l)
    c=k/n 
    if c in l:
        print((l.index(c)+1))
    else:
        print('Impossible')