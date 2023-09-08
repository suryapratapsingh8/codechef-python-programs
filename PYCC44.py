# cook your dish here
n = int(input())
for i in range(n):
    S, X, Y, Z = [int(x) for x in input().split()]
    if X+Y+Z<=S:
        print(0)
    elif X+Z<=S or Y+Z<=S:
        print(1)
    else:
        print(2)