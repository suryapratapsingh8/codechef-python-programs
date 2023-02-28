
for i in range(int(input())):
    s=int(input())
    a=list(map(int,input().split()))
    x=0
    y=0
    for i in range(s):
        for j in range(i+1,s):
            if a[i]>a[j]:
                x+= 1
    for k in range(s-1):
        if a[k]>a[k+1]:
                y+= 1
    
    if x==y:
        print('YES')
    else:
        print('NO')
        
            
        
        