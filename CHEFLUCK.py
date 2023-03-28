t=int(input())
for _ in range(t):
    N=int(input())
    if N%7==0 and N%4!=0:
        print(N)
    else:
        if N<11 and N%4!=0 and N%7!=0:
            print(-1)
        else:
            while N%7!=0:
                N=N-4
            print(N)
                
        