for _ in range(int(input())):
    n, m = map(int, input().split())
    s = dict()
    for _ in range(n):
        c, l = map(int, input().split())
        if l in s:
            s[l] += -c
        else:
            s[l] = -c
    for _ in range(m):
        c, l = map(int, input().split())
        s[l] += c
    m = 0
    for i in s:
        if s[i] > 0:
            m += s[i]
    print(m)