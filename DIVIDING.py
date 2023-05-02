n = int(input())
c = list(map(int,input().split()))
count = 0
for i in c:
    count = count + i
if count == n*(n + 1) // 2:
    print("YES")
else:
    print("NO")