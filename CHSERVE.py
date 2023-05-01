# cook your dish here
for _ in range(int(input())):
    p1, p2, k = map(int,input().split())
    print('COOK' if ((p1+p2)//k)%2 else 'CHEF')