# Bowling strategy
for _ in range(int(input())):
    n, k , l = map(int, input().split())
    if(k*l < n or (k == 1 and n > 1)):
        print(-1)
    else:
        value = 1
        lt = []
        for i in range(n):
            lt.append(value)
            if((i+1) % k == 0):
                value = 1
                continue
            value += 1
        print(*lt)
        