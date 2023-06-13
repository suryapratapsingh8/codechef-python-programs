# cook your dish here
from collections import Counter
t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    ob=Counter(l)
    x=[int(x) for x in ob.values()]
    print(len(l)-max(x))