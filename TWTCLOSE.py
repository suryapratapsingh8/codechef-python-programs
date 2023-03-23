n, k = list(map(int, input().split()))

d = dict()
for i in range(k):
    l = (input().strip().split())
    if(l[0] == "CLOSEALL"):
        d = dict()
    else:
        if(l[1] in d):
            del d[l[1]]
        else:
            d[l[1]] = 1

    print(len(d))