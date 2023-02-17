# cook your dish here
# cook your dish here

from statistics import mode

for _ in range(int(input())):
    n = int(input())
    k = list(map(int,input().split()))
    j = mode(k)
    cn = k.count(j)
    print(n-cn)