t=int(input())
for i in range(0,t):
    p,q = map(int,input().split())
    li= list(range(1,p+1))
    x= q-p+1
    if(x<1):
        print(-1)
    else:
        li.remove(x)
        li.insert(0,x)
        print(*li)