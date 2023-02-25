# cook your dish here
for _ in range(int(input())):
    n,m=map(int,input().split())
    x,y=map(int,input().split())
    l=[]
    for i in range(n):
        s=input()
        a=s.count('P')
        b=s.count('F')
        if b>=x:
            l.append('1')
        elif b==x-1 and a>=y:
            l.append('1')
        else:
            l.append('0')
    print(''.join(l))