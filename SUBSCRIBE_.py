# cook your dish here
import math
t = int(input())
for i in range(t):
    n, x = map(int, input().split())
    subscription = math.ceil(n/6)
    print(subscription*x)