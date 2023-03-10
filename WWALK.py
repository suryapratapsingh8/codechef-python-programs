# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x,y=0,0
    f=0
    wd=0
    for i in range(n):
        if l1[i]==l2[i]:
            if x==y:
                wd=wd+l1[i]
        else:
            x=x+l1[i]
            y=y+l2[i]
    print(wd)