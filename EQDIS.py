t=int(input())
for k in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    f=len(a)
    b=set(a)
    #print(a)
    d=len(b)
    if d&1==0 or d<n:
        print("YES")
    else :
        print("NO")