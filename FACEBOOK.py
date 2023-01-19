t=int(input())
for T in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    brr=list(map(int,input().split()))
    temp=max(arr)
    ans=0
    comment=0
    for i in range(n):
        if arr[i]==temp and comment<brr[i]:
            ans=i
            comment=brr[i]
    print(ans+1)
