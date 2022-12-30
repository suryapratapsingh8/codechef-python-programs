# CHEF AND DEMONETISATION
for _ in range(int(input())):
    s,n=map(int,input().split())
    if s&1==0:
        if s%n!=0:
            print((s//n)+1)
        else:
            print(s//n)
    else:
        if (s-1)%n!=0:
            print((s//n)+2)
        else:
             print((s//n)+1)