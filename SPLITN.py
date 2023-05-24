# cook your dish here
from math import log

for _ in range(int(input())):
    n = int(input())
    ans = []
    while n>0:
        res = round(log(n,2),14)
        ans.append(int(res))
        n -= 2**ans[-1]

    print(len(ans)-1)