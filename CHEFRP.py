for _ in range(int(input())):
    
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)

    if arr[n-1] == 1:
        print(-1)
    elif n == 1:
        print(2)
    else:
        print(sum(arr) - arr[n-1] + 2)