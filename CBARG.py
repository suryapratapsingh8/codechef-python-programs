for _ in range(int(input())):
    n = int(input())
    m = [int(x) for x in input().split()] 
    ans = m[0]
    for i in range(1, n):
        ans += max([m[i] - m[i-1], 0])
    print(ans)
    