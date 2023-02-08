# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    m=1000000000
    for i in range(1,n):
        c=l[i]-l[i-1]
        if c<m:
            m=c 
    print(m)