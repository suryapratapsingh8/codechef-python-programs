T = int(input())
for _ in range(T):
    N, M, C = map(int, input().split())
    ans = 0
    for i in range(1, C + 1):
        if C % i == 0:
            if i <= N and C // i <= M:
                ans += 1
    print(ans)