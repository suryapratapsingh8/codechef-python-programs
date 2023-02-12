
t = int(input())
for _ in range(t):
    M,x,y = [int(x) for x in input().split()]
    houses= [int(x)-1 for x in input().split()]
    mark = [0 for _ in range(100)]
    low = 0 
    high = 0 
    houses = list(sorted(houses))
    n = x*y
    for h in houses:
        low = max(h-x*y,0)
        high = min(h+x*y,99)
        for j in range(low,high+1):
            mark[j] = 1 
    print(100-sum(mark))
    
        