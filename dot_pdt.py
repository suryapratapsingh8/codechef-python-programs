l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l1.sort()
l2.sort()
n1=len(l1)
n2=len(l2)
sum=0
for i in range (n2):
    sum=sum+l1[n1-1-i]*l2[n2-1-i]
print(sum)
