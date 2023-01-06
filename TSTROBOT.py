# cook your dish here
for _ in range(int(input())):
    n, x = map(int,input().split())
    s = input()
    r= [x]
    for i in s:
        if i == "R":
            x = x + 1
        elif i == "L":
            x = x - 1
        r.append(x)
    p= max(r)
    q = min(r)
    print(p - q + 1)
    