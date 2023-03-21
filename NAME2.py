for _ in range(int(input())):
    m,w=list(map(str, input().split()))
    if len(m)>=len(w):
        x,y=m,w
    else:
        x,y=w,m
    if y[0] in x:
        x=x[1:len(x)]
        for j in range(1,len(y)):
            if y[j] not in x:
                print("NO")
                break
            x=x[x.index(y[j])+1:len(x)]
        else:
            print("YES")
    else:
        print("NO")