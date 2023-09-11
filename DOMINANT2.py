# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ob=Counter(l)
    k=[x for x in ob.values()]
    m=max(k)
    if k.count(m)==1:
        print('YES')
    else:
        print('NO')