# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    a=sum(s)
    if a<0:
        print("NO")
    else:
        print("YES")