# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    lst = list(map(int,input().split()))
    dict={}
    for i in range(0,n):
        if(lst[i] in dict):
            dict[lst[i]]+=1;
        else:
            dict[lst[i]]=1;
    ans=0
    for key,value in dict.items():
        ans=max(ans,value)
    if(ans > (n+1)/2 ):
        print("NO")
    else:
        print("YES")
    
        
    