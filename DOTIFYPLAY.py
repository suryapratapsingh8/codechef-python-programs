t = int(input())
for _ in range(t):
    n,k,l = list(map(int,input().split()))
    arr = []
    for i in range(n):
        a,b = list(map(int,input().split()))
        if b==l:
            arr += [a]
    arr.sort(reverse=True)
    if len(arr)<k:
        print(-1)
    else:
        print(sum(arr[:k]))
            
                    