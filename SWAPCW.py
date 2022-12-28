# Swapping chef ways
t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    s = list(s)
    s1 = sorted(s)
    for i in range(int(n/2)):
        if ord(s[i]) > ord(s[n-i-1]):
            s[i], s[n-i-1] = s[n-i-1],s[i]
    if s == s1:
        print("YES")
    else:
        print("NO")