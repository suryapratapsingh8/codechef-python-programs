# version control system
#surya pratap singh
for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c1=c2=0
    for i in a:
        if i in b:
            c1+=1
    for j in range(1,n+1):
        if j not in a and j not in b:
            c2+=1
    print(c1,c2)