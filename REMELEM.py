# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    j=n-1
    while(j!=0):
        if(a[0]+a[j]<=k):
            j-=1
        else:
            print('NO')
            break
    else:
        print('YES')