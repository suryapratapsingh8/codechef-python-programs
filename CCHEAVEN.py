# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    f=0
    c=0
    d=0
    for i in s:
        if i=='1' and f==1:
            c=c+1 
            if c>=d:
                print('yes')
                break 
        elif i=='1' and f==0:
            c=c+1 
            if c>d:
                f=1 
                print('yes')
                break
        else:
            d=d+1
            f=1
    else:
        print('no')
                
    
    
        
    