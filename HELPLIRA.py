# cook your dish here
n=int(input())

l=[]
    
for i in range(n):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))*0.5
    l.append(a)
maxi=l[0];mini=l[0]
mx,mn=0,0
for i in range(n):
    if maxi<=l[i]:
        maxi=l[i]
        mx=i+1
    if mini>=l[i]:
        mini=l[i]
        mn=i+1
print(mn,mx)        
    
    
    