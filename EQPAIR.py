# cook your dish here
from math import comb
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    c = Counter(a)
    
    ans = 0
    for num in c:
        ans += comb(c[num], 2)
        
    print(ans)