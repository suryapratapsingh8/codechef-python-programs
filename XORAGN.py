for _ in range(int(input())):
    
    N = int(input())
    A = list(map(int, input().split()))
    
    res = 0
    for i in range(N):
        res = res ^ (2*A[i])
    print(res)
        