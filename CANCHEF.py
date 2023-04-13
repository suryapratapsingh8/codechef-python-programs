# cook your dish here
for _ in range(int(input())):
    x, y = map(int, input().split())
    if (2*y)<=(x*15):
        print('YES')
    else:
        print('NO')