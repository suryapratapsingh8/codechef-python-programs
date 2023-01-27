# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a>=b and a>=c:
        if a==b+c:
            print('Yes')
        else:
            print('No')
    elif b>=a and b>=c:
        if b==a+c:
            print('Yes')
        else:
            print('No')
    else:
        if c==b+a:
            print('Yes')
        else:
            print('No')