# cook your dish here
app = int(input())
for a in range(app):
  s,x,y,z=map(int,input().split())
  if x+y+z<=s: print(0)
  elif x+z<=s or y+z<=s: print(1)
  else: print(2)