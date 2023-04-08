# cook your dish here
t = int(input())
for i in range(t):
    a, b, m = map(int, input().split())
    s = max(b, a) - min(a, b)
    b = m - max(b, a) + min(a, b)
    print(min(b,s))