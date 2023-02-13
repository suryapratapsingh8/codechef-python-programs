n=int(input())
l=list(map(int,input().split()))
wat=[]

for i in range(n-1):
    for j in range(i+1,n):
        p=min(l[i],l[j])
        k=p*(abs(j-i))
        wat.append(k)
print(max(wat))