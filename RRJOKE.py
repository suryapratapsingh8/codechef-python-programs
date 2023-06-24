# cook your dish here
import operator
for _ in range(int(input())):
    n = int(input())
    pts = []
    for i in range(n):
        pts.append(tuple(map(int,input().split())))
    y = 1
    for i in range(2,n+1):
        y = y ^ i
    else:
        print(y)