# cook your dish here
for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input().strip()
    if s[0] == '0':
        s = '1' + s[1:]
        k -= 1
    s += '0' * k
    print(s)
    
