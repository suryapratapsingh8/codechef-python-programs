# cook your dish here
for _ in range(int(input())):
    n, x = map(int,input().split())
    a = list(map(int,input().split()))
    p = x
    maxp = x
    for m in a:
        p += m
        maxp = max(maxp,p)
    print(maxp)