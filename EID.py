# cook your dish here
for I in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    s=sorted(a)
    m=1000000
    for i in range(n-1):
        x=s[i+1]-s[i]
        if x<m:
            m=x 
    print(m)