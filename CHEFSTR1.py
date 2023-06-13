# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    s=0
    for i in range(1,n):
        s+=abs(l[i]-l[i-1])-1
    print(s)