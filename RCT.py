# cook your dish here

t = int(input())
for _ in range(t):
    l, h = map(int, input().split())
    if (l * h) & 1 == 0:
        print("YES")
    else:
        print("NO")