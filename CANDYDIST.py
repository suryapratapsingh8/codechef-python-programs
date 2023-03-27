#Enter your code here
for _ in range(int(input())):
    n,m=map(int,input().split())
    k=n//m 
    if k&1==0 and n%m==0:
        print('Yes')
    else:
        print('No')