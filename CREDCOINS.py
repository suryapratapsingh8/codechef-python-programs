# cook your dish here
import math
T= int(input())
for X in range(T):
    X,Y= map(int,input().split())
    print(math.floor((X*Y)/100))