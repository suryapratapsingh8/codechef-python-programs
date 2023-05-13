n=int(input())
for i in range(n):
    s = int(input())
    l = list(input())
    e = l[::2]
    o = l[1::2]
    e.sort()
    o.sort()
    if e == o:
        print("YES")
    else:
        print("NO")