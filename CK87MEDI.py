t=int(input())
for i in range(t):
    n,k=map(int,input().split(' '))
    a=list(map(int,input().split(' ')))
    a.sort()
    print(a[(n+k)//2])