
t = int(input())

for i in range(t):
    n,m,x = map(int, input().strip().split())
    l = n*2
    b = m*2
    area = l+b
    cost = area*x
    print(cost)
