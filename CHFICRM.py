t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    flag=0
    s={'5':0 ,'10':0}
    for i in a:
        if i==5:
            s['5']+=1 
        elif i==10:
            if s['5']>=1:
                s['5'] -= 1
                s['10'] += 1
                continue
            else:
                flag=-1
                break
        else:
            if s['10']>=1:
                s['10'] -= 1
            elif s['5']>=2:
                s['5'] -=2
            else:
                flag=-1
                break
    print('YES' if flag==0 else 'NO')