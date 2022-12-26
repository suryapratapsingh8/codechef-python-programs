t=int(input())
for _ in range(t):
    N=int(input())
    sum = (N*(N+1))/2
    if sum%2==0:
        print(N)
    else:
        print(N-1)