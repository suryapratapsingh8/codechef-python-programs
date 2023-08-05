# cook your dish here
for i in range(int(input())):
    o=int(input())
    p=list(map(int,input().split()))
    j=sorted(p)
    k=sum(p)
    t=o-1
    print(k,end=' ')
    for m in range(t):
        k=k-j[m]
        print(k,end=' ')
    print()