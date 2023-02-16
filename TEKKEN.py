# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    k=abs(b-c)
    if a>k:
        print('Yes')
    else:
        print('No')