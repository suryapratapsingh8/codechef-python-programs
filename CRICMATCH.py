# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    k=m*36
    if k>=n:
        print('YES')
    else:
        print('NO')