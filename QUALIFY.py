T = int(input())
for tc in range(T):
   X,A,B=input().split()
   X=int(X)
   A=int(A)
   B=int(B)
   N=int(A+(B*2))
   if(N>=X):
      print("Qualify")
   else:
      print("NotQualify")
