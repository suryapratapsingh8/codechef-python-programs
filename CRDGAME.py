# cook your dish here
for _ in range(int(input())):
    n = int(input())
    c,m = 0,0
    for i in range(n):
        sma,smb=0,0
        a,b = map(int,input().split())
        sma = sum([int(i) for i in str(a)])
        smb = sum([int(i) for i in str(b)])
        if sma > smb: 
            c += 1
        elif sma < smb:
            m += 1
        elif sma == smb:
            c += 1
            m += 1
        
    if c > m:
        print(0,c)
    elif c < m:
        print(1,m)
    elif c ==m:
        print(2,m)
        
        
    