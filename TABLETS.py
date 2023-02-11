# cook your dish here
for t in range(int(input())):
    x, y = map(int, input().split())
    print("Yes" if (y >= x * 3) else "No")