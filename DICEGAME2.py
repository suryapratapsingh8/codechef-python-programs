# cook your dish here
dice=int(input())
for i in range(dice):
  a,b,c,d,e,f=map(int,input().split())
  alice=(a+b+c)-min(a,b,c)
  bob=(d+e+f)-min(d,e,f)
  if alice>bob:print("alice")
  elif bob>alice:print("bob")
  else:print("tie")