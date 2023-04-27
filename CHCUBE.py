for _ in range(int(input())):
    f,b,l,r,t,bt = map(str,input().split())
    if ((f==l or f==r) and (f==t or f==bt)) or ((b==l or b==r) and (b==t or b==bt)):
        print("YES")
    else:
        print("NO")