
for _ in range(int(input())):
    n = int(input()) 
    t = 0
    for __ in range(n):
        x, l, f = map(int, input().split()) 
        if t < x:
            t = x
        if (t-x)%f:
            t += f-(t-x)%f
        t += l
    print(t)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    