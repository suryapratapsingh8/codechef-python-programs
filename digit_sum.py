n=int(input())
l=[]
c=0
s=0
for i in range(10):
    if n>0:
        k=n%10
        s=s+k
        c=c+1 
    else:
        s=s+n
        c=c+1
        break
print(c,s)

    
