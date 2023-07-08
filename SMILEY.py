t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    col = 0
    ans = 0
    prev = None
    for i in s:
        if i==":":
            if col and i!=prev:
                ans += 1
            col = 1
        elif i=="(":
            col = 0
        prev = i
    print(ans)