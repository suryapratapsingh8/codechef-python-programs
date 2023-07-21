# cook your dish here
import math
t = int(input())
for _ in range(t):
    x,y,r = map(int, input().split())
    gift = r//30
    if r==0:
        print(math.ceil(x/y))
    else:
        total = x + gift
        print(math.ceil(total/y))
        
        