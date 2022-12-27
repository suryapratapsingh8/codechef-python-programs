# THE ONE WITH THE RUSS
for _ in range (int(input())):
    n,x,k=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    m=0
    for i in range(n):
        if abs(l1[i]-l2[i])<=k:
            m=m+1
    if m>=x:
        print('YES')
    else:
        print('NO')