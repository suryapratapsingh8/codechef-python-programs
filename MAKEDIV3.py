# make it divisible
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print('3')
    else:
        
      c=('1'+'0'*(n-1))
      d=int(c)
      e=d-1 
      print(e+6)
