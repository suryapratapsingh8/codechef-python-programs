# cook your dish here
for _ in range(int(input())):
    s = input()
    for l in s:
        if s.count(l) == len(s) - s.count(l):
            print('YES')
            break
    else:
        print('NO')