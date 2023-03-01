# cook your dish here
for tc in range(int(input())):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    P.sort(reverse = True)
    maxsum = 0
    count = 0
    for i in range(N):
        maxsum += P[i]
        count += 1 
        if maxsum >= M:
            break
    if maxsum >= M:
        print(count)
    else:
        print(-1)
        
