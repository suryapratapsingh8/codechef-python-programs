t = int(input())

for case in range(t):
    a, b = map(int, input().split())
    c = 0
    
    while (b % a != 0):
        if (a % 2 == 0):
            a = a // 2
        else:
            a = (a - 1) // 2
        c += 1
    while (a != b):
        a = a * 2
        c += 1
    print(c)
