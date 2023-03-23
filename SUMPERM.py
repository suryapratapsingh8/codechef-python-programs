for _ in range(int(input())):
    N=int(input())
    if N%2==1:
        print(-1)
    else:
        ans=[]
        for i in range(1,N+1,2):
            ans.append(i+1)
            ans.append(i)
        print(*ans)
        
        