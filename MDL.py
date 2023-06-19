# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = tuple(zip(map(int,input().split()),range(n)))
    minmax = sorted((min(a),max(a)),key = lambda x: x[1])
    print(*[i for i, j in minmax])