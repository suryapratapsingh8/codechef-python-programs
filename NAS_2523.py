for _ in range(int(input())):
    n=int(input())
    if n%2!=0:
        print(-1)
    else:
        while(n):
            print(n,end=" ")
            n=n-1
        print()    