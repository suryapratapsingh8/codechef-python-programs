
from collections import Counter
for _ in range(int(input())):
    s=int(input())
    l=list(map(int,input().split()))
    dic=Counter(l)
    dic2={}
    for i,j in dic.items():
        if j in dic2:
            dic2[j]+=1
        else:
            dic2[j]=1
    m=max(dic2.values())
    maxi=float("inf")
    for i,j in dic2.items():
        if j==m:
            maxi=min(maxi,i)
    print(maxi)