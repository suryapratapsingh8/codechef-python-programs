# cook your dish here
for _ in range(int(input())):
    p,s = map(int,input().split())
    
    x = (p - (p ** 2 - 24 * s) ** 0.5) / 12
    h = (p - 8 * x) / 4
    
    print(round(x * x * h, 2))