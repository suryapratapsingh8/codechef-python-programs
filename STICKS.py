# cook your dish here
for _ in range(int(input())):
    x = int(input())
    l = list(map(int,input().split()))
    l.sort()
    l1 = l[::-1]
    s = set(l1)
    c = 0
    d = []
    for i in s:
        for j in range(l1.count(i)//2):
            d.append(i)

    if len(d)>=2:
        print(d[-2]*d[-1])
    else:
        print(-1)
    