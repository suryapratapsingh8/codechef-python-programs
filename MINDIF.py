# cook your dish here
# cook your dish here

t = int(input())

for cases in range(t):
    N = int(input())
    Arr = list(map(int, input().split(' ')))
    if N == 2:
        print(-1)
        continue 
    Arr.sort()
    if Arr[-1] == Arr[0]:
        print(-1)
        continue 
    min_diff = min(Arr[i + 1] - Arr[i] for i in range(N - 1))
    if Arr[1] == Arr[-1]: 
        print(Arr[1], Arr[0], *Arr[2:])
    elif Arr[0] == Arr[-2]:
        print(*Arr[:-2], Arr[-1], Arr[-2])
    elif Arr[1] - Arr[0] == min_diff:
        print(Arr[-1], *Arr[:-1])
    else:
        print(*Arr[1:], Arr[0])
        
                
            
        
        
            
        