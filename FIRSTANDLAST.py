# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    s=a[0]+a[-1]
    for i in range(n-1):
        s=max(s,a[i]+a[i+1])
    print(s)