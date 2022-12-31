# MAke A and B equaal
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    if sum(a)!=sum(b):
        print(-1)
    else:
        k = 0
        for j in range(n):

            k += abs(a[j] - b[j])
        print((k) // 2)
