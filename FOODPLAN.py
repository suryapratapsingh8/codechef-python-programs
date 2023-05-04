t = int(input())
for i in range(t):
    n,m = map(int,input().strip().split())
    n = n - 10/100*n
    if (n>m):
        print("DINING")
    elif(n<m):
        print("ONLINE")
    else:
        print("EITHER")