# cook your dish here
import math
for _ in range(int(input())):
    n,k=map(int,input().split())
    print(math.ceil(n/k))