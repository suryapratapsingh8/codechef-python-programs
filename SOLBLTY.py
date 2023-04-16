T=int(input())
for i in range(T):
    X,A,B=map(int,input().split())
    S=A+(100-X)*B
    print(S*10)