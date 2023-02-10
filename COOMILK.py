# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=input().split()
    ans="YES"
    for i in range(n-1):
        if s[i]=="cookie" and s[i+1]=="cookie":
            ans="NO"
    if s[-1]=="cookie":
        ans="NO"
    print(ans)
    
        
    
