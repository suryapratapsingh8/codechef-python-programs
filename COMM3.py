# cook your dish here
t=int(input())
def distance(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(map(int,input().split()))
    ab=distance(a,b)
    bc=distance(b,c)
    ca=distance(c,a)
    l=[ab,bc,ca];s=0
    for i in l:
        if i>n:
            s+=1
    if s>1:
        print('no')
    else:
        print('yes')