# CHEF AND SALARY PAY
for _ in range(int(input())):
    x,y=map(int,input().split())
    l=list(map(int,input()))
    m=0
    c=0
    d=0
    for i in l:
        if i==1:
            c=c+1 
            d+=1  
        else:
            if d>m:
                m=d
                d=0
            else:
                d=0
    if d>m:
        m=d
    
    print((c*x)+m*y)