T = int(input())
for _ in range(T):
    P,M,V = map(int,input().split())
    print((M-(P-1))*V)