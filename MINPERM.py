# cook your dish here
for _ in range(int(input())):
    n = int(input())
    k = n+1 if n%2 else n
    arr = []
    for i in range(1,k,2):
        arr.extend([i+1, i])
    if n%2:
        arr[-3], arr[-1] = arr[-1], arr[-3]
        arr.pop(-2)
    print(*arr)
    
    