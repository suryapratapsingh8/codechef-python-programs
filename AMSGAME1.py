def gcd(x,y):
    while(y):
        x,y = y , x % y
    return abs(x)
    
for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int,input().split()))
    
    ans = l1[0]
    
    for i in range(1,len(l1)):
        ans = gcd(ans,l1[i])
    print(ans)