# cook your dish here
import math
n=int(input())
l=list(input())
v=0
for i in range(n):
    if l[n-i-1]=='1':
        v=v+pow(2,i)
c=0
while(v&1==0):
    v=v//2
    c=c+1 
print(c)