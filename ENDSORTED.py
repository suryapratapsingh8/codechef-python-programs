# cook your dish here

for _ in range(int(input())):

    n = int(input())
    p = list(map(int,input().split()))
    loc1 = p.index(1)
    locn = p.index(n)
    #print(n - 1 - locn,'+', loc1,'-', int(loc1>locn))
    print(n - 1 - locn + loc1 - int(loc1>locn))