for i in range(int(input())):
    p,m=map(str,input().split())
    par = p+m
    name=""
    for i in range(int(input())):
        name += input()
    res=True
    for char in name:
        if char in par:
            par = par.replace(char, "", 1)
        else:
            res=False
    print("YES" if res else "NO")