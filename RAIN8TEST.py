# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    f=0
    c=0
    for i in range(n):
        k=int(input())
        if f==0 and k==0:
            continue 
        elif f==0 and k==1:
            c=c+x
            f=1 
        elif f==1 and k==0:
            c=c+x 
            f=0 
        elif f==1 and k==1:
            c=c+x 
    print(c)