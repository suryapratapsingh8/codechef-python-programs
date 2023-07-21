# cook your dish here
hotel=int(input())
for h in range(hotel):
  g,c=map(int,input().split())
  if c==0: print(g)
  elif g==c: print(2*g-1)
  else: print((g-c)+(2*c))