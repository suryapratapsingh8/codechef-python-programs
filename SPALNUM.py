# cook your dish here
t=int(input())
for i in range(t):
    a, b = map(int,input().split())
    sumu = 0
    for i in range(a,b+1):
        j = str(i)
        if j == j[::-1]:
            sumu += i
    print(sumu)        