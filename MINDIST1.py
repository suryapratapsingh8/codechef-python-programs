t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    a = b = False
    for i in range(n):
        if s[i]=='1':
            if i%2:
                a = True
            else:
                b = True
    print(1 if a&b else 2)