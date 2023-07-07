t = int(input())
for i in range(t):
    N,X,Y = map(int,input().split())
    s = X + Y*2
    if (s<=N):
        print("YES")
    else:
        print("NO")