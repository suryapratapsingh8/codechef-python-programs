# Print pattern
t = int(input())

for i in range(t):

    n = int(input())
    k = 1
    
    q = [None] * n
    
    for i in range(n):
        k += i
        q[i] = k
    print(*q)
    
    for i in range(n - 1):
    
        for j in range(n - 1):
            q[j] = q[j+1] + 1
        
        q[n - 1] = q[n-2] + (n - i - 1)
        print(*q)