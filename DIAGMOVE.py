# cook your dish here
for _ in range(int(input())):
    x, y = map(int,input().split())
    print('Yes' if (x+y)%2 == 0 else 'No')