# cook your dish here
for i in range(int(input())):
    n,m,x=map(int,input().split())
    if m==x:
        print(0)
    else:
        print((x*n)//(x+1))