# cook your dish here
for _ in range(int(input())):
    x, y, k = map(int,input().split())
    print('Paja' if (x+y)//k%2 else 'Chef')