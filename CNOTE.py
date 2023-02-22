# cook your dish here
for _ in range(int(input())):
    x,y,k,n=map(int,input().split())
    
    f=1
    while  n>0:
        n-=1
        p,c=map(int,input().split())
        if  p>=x-y  and c<=k:
            f=0
            
    if f==0:print('LuckyChef')
    else:print('UnluckyChef')