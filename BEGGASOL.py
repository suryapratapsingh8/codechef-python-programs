# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    g=l[0]
    d=0
    for i in range(1,n):
        if g!=0:
            g=g-1
            d=d+1 
            g=g+l[i]
    print(g+d)
        