# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    if n&1==0:
        print((a*n//2)+(b*n//2))
    else:
        k=n//2
        print((a*k)+(k+1)*b)