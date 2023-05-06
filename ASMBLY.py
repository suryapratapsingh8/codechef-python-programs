# cook your dish here
n=int(input())
l=list(map(int,input().split()))
c=1 
m=l[0]
for i in range(1,n):
    if l[i]>m:
        c=c+1 
        m=l[i]
print(c)