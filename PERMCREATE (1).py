t=int(input())
for i in range(t):
    n=int(input())
    if n<=3:
        print(-1)
    else:
        for j in range(2,n+1,2):
            print(j,end=" ")
        for k in range(1,n+1,2):
            print(k,end=" ")
        print()