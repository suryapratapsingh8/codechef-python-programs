# cook your dish here
import math
for _ in range(int(input())):
    a,b,n=map(int,input().split())
    if n&1==0:
        if abs(a)>abs(b):
            print('1')
        elif abs(a)<abs(b):
            print('2')
        else:
            print('0')
    else:
        if a>b:
            print('1')
        elif b>a:
            print('2')
        else:
            print('0')