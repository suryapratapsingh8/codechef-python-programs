n,h,x=map(int,input().split())
l=list(map(int,input().split()))
ans="NO"
for i in l:
    if i+x>=h:
        ans="YES"
        break 
print(ans)