for _ in range(int(input())):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    x = 0
    for a in l:
        if a < k:
            x += k-a
        else:
            x += min(a%k, k-a%k)
    print(x)