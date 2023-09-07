# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    s=0
    for i in range(0,n,2):
        s=s+l[i]
    print(s)
        

