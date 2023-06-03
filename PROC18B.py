# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort(reverse=True)
    k=l[0]
    for i in range(1,n):
        k=(k+l[i])/2
    print(k)