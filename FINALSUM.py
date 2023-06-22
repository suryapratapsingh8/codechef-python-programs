# cook your dish here
for _ in range(int(input())):
    n, q = map(int,input().split())
    a = sum(list(map(int,input().split())))
    for i in range(q):
        s, f = map(int,input().split())
        if (f-s+1)%2:
            a += 1
    else:
        print(a)