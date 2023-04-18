# cook your dish here
for _ in range(int(input())):
    X=int(input())
    s=input()
    c,n=0,0
    for i in s:
        if i=='C':
            c+=2
        elif i=='N':
            n+=2
        else:
            c+=1
            n+=1
    print(55*X if c==n else(60*X if c>n else 40*X))