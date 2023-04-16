import math
# cook your dish here
t = int(input())
while t>0:
    n,k = map(int,input().split())
    print(math.comb(n-1,k-1))
    t -= 1