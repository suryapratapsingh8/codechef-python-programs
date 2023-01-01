#RED ALERT
for _ in range (int(input())):
    n,d,h=map(int,input().split())
    l=list(map(int,input().split()))
    a=0 
    
    for i in range(n):
        if l[i]!=0:
            a=a+l[i]
            if a>h:
                print('YES')
                break 
        elif l[i]==0 and a>=d:
            a=a-d 
        else:
            a=0
    else:
        print('NO')