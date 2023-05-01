t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int, input().split()))
    l = []
    for i in range(n):
        c = 0
        for j in range(i+1, n):
            if x[j] > x[i]:
                c += 1
        l.append(c)
    print(*l)