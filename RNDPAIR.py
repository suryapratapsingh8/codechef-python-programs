# cook your dish here
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    a = sorted(list(map(int,input().split())))
    big = a.count(a[-1])
    sec = a.count(a[-2])
    if big == 1:
        print(sec/(n*(n-1)/2))
    else:
        print((big*(big-1)/2)/(n*(n-1)/2))