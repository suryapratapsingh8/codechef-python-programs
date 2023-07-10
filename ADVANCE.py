# cook your dish here
rate=int(input())
for r in range(rate):
  X,Y=map(int,input().split())
  if X<=Y<=X+200:print("yes")
  else:print("no")