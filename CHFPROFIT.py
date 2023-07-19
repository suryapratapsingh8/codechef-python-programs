# cook your dish here
profit=int(input())
for p in range(profit):
  x,y,z=map(int,input().split())
  print(x*abs(y-z))