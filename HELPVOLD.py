
n=int(input())
l=list(map(int,input().split()))
l.sort()
c=0
for i in range (n-1):
    c+=l[i]*l[i+1]
print(c)  