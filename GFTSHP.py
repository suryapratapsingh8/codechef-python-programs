for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    sum1=0
    ans=0
    i=0
    while i<n:
        if sum1+a[i]<=k:
            sum1+=a[i]
            ans+=1 
            i+=1 
        else:
            if sum1+((a[i])/2)<=k:
                ans+=1 
            i=n
    print(ans)