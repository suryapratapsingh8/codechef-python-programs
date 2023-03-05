n=int(input())
m,c=map(int,input().split())
l=0
r=0
for i in range(n):
        x,y,p=map(int,input().split())
        k=m*x+c 
        if k>y:
            l=l+p 
        else:
            r=r+p 
if l>r:
        print(l)
else:
        print(r)
                
        