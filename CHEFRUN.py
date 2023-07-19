# cook your dish here
rest=int(input())
for r in range(rest):
  a,b,c,d,e=map(int,input().split())
  chef=(c-a)/d
  kefa=(b-c)/e
  if chef<kefa:print("Chef")
  elif kefa<chef:print("Kefa")
  else: print("Draw")