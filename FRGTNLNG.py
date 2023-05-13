t = int(input())
for i in range(t):
    N,K = map(int,input().split())
    N_strings = list(map(str,input().split()))
    r = []
    for i in range(0,K) :
        l =[m for m in input().split()]
        l_s = l[0]
        l_v = l[1:]
        r = r + l_v
    r = set(r)
    for i in N_strings :
        if i in set(r) :
            print('YES',end = ' ')
        else :
            print('NO',end = ' ')
        print()
    