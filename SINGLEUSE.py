for _ in range(int(input())):
    h,x,y=map(int,input().split())
    k=h-y
    c=1 
    while (k>0):
        k=k-x
        c=c+1 
    print(c)
