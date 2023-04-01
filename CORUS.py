from collections import Counter
for _ in range(int(input())):
    n,q=map(int, input().split())
    s=input()
    d=Counter(s)
    t=set(s)
    p=0
    for i in range(q):
        c=int(input())
        for j in t:
            if d[j]>c:
                p+=d[j]-(c)
        print(p)
        p=0