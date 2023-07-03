# cook your dish here
phone = int(input())
for p in range(phone):
  R,B = map(int, input().split())
  if R<B: print("repair")
  elif B<R: print("new phone")
  else:print("any")