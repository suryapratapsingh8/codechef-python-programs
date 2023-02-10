# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    l=list(map(int,input().split()))
    l.sort()
    if l[n-1]>=x:
        print('YES')
    else:
        print('NO')