
for _ in range(int(input())):
    ans = 0
    for __ in range(int(input()) ):
        s, v, p = map(int, input().split()) 
        ans = max([ans, v//(s+1)*p])
    print(ans)