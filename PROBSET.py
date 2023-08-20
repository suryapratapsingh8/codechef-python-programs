# cook your dish here
for i in range(int(input())):
    n, m = map(int, input().split())
    s = []
    for i in range(n):
        s.append(input().split())
    s.sort()
    res = ""
    for i in s:
        if i[0] == "correct" and '0' in i[1]:
            res = "INVALID"
            break
        elif i[0] == "wrong" and '0' not in i[1]:
            res = "WEAK"
            break
    if res == "":
        print("FINE")
    else:
        print(res)