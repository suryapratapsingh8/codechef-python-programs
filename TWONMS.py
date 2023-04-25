t=int(input())
for  _ in range(t):
    A,B,N=map(int,input().split())
    A=A*(2**(N%2))
    B=B
    if A>B:
        print(A//B)
    else:
        print(B//A)
            