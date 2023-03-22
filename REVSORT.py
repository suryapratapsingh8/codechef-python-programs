t=int(input())
for i in range(t):
    n,x= map(int, input().split())
    a = list(map(int, input().split()))
    b,c=0,0
    for i in a:
        if i < b:
            if i > x-b:
                c = 1
        else:
            b = i
    if c == 1:
        print('NO')
    else:
        print('YES')