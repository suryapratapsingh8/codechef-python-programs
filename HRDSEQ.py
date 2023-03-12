# cook your dish here
t=int(input())
for t in range(t):
    n=int(input())
    l=[0]
    while len(l)<n:
        x=l[-1]
        k=-1
        for i in range(len(l)-2,-1,-1):
            if l[i]==x:
                k=i
                break
        if k==-1:
            l.append(0)
        else:
            l.append(len(l)-1-k)
    print(l.count(l[-1]))