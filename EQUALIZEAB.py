# cook your dish here
for _ in range(int(input())):
    a,b,x=map(int,input().split())
    c=abs(a-b)
    if c%(2*x)==0:
        print('YES')
    else:
        print('NO')