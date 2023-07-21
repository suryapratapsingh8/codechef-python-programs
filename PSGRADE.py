# cook your dish here
exam=int(input())
for e in range(exam):
  am,bm,cm,p,a,b,c=map(int,input().split())
  if (a>=am and b>=bm and c>=cm) and (a+b+c)>=p: print("yes")
  else: print("no")