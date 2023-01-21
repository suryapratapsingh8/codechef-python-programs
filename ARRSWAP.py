# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l=l1+l2
    l.sort()
    m = l[n-1]-l[0]
    for i in range (1,n+1):
        m = min(m,(l[i+n-1]-l[i]))
    print(m)
    
