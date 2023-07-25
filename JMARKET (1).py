# cook your dish here
fruit=int(input())
for f in range(fruit):
 x,a,b,c=map(int,input().split())
 m=min(a,b,c)
 mx=max(a,b,c)
 print((x-1)*m+(a+b+c-m-mx))