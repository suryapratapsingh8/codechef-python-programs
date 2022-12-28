# EQUAL COINS
for _ in range (int(input())):
    x,y=map(int,input().split())
    if x&1!=0:
        print('NO')
    elif x==0 and y&1!=0:
        print('NO')
    else:
        print('YES')
    