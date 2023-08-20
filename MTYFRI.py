for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    c1, c2 = sorted(a[::2], reverse = True), sorted(a[1::2])
    
    for i, j, l in zip(range(len(c1)), range(len(c2)), range(k)):
        if c1[i] <= c2[j]:
            break
        c1[i], c2[j] = c2[j], c1[i]
    
    print("YES") if sum(c2) > sum(c1) else print("NO")