# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l1=sorted(l)
    a=0
    b=n-1
    for i in range(n):
        if i%2==0:
            l[i]=l1[a]
            # print(*l,' even')
            a+=1
        else:
            l[i]=l1[b]
            # print(*l,' odd')
            b-=1
    print(*l)