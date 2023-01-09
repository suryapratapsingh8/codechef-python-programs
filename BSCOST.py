# cook your dish here
a=[]
for i in range(int(input())):
    n,tx,ty=map(int,input().split())
    s=input()
    if(tx<=ty):
        a=sorted(s)
        b=''.join(a)
        n=b.count('10')
        m=b.count('01')
    else:
        c=sorted(s,reverse=True)
        d=''.join(c)
        n=d.count('10')
        m=d.count('01')
    print(m*tx+n*ty)