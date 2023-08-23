for t in range(int(input())):
  n=int(input())
  a=[]
  b=[]
  c=[]
  if(n%2==0):
    l=list(range(1,n+1))
    l1=l[:n//2]
    l2=l[n//2:]
    l1=l1[::-1]
    for i in range(n//2):
      c.append(l2[i])
      c.append(l1[i])
    print(*c)
  else:
    l=list(range(1,n))
    l1=l[:n//2]
    l2=l[n//2:]
    l1=l1[::-1]
    for i in range(n//2):
      c.append(l2[i])
      c.append(l1[i])
    c.append(n)
    print(*c)
    
      
    