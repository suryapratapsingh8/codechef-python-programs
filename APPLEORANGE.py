
import math
for i in range(int(input())):
    n,m=map(int,input().split())
    ans=math.gcd(n,m)
    print(ans)