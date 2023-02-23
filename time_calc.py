h,m,s=map(int,input().split())
x,y,z=map(int,input().split())
k=s+z
l=m+y 
g=h+x 
if k>=60:
    k=k-60 
    l=l+1 
    if l>=60:
      l=l-60
      g=g+1 
    else:
        l=l
elif k<60 and l>=60:
    l=l-60
    g=g+1
print(g,l,k)