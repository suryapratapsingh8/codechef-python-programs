# cook your dish here
for _ in range(int(input())):
    n = int(input())
    
    come = [int(x) for x in input().split()]
    go   = [int(x) for x in input().split()]
    
    time = 0
    maxcount = 0
    count = 0
    while (time <= max(max(come), max(go))):
        if (time in come):
            count += come.count(time)
        if (time in go):
            count -= go.count(time)
        
        if (count > maxcount):
            maxcount = count
            
        time += 1
    
    print(maxcount)
    
    