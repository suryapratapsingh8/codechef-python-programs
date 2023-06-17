# cook your dish here
for _ in range(int(input())):
    s = input()
    if s[0] == 'x':
        res = s.count('xy')
        s = s.replace('xy','')
        res += s.count('yx')
    else:
        res = s.count('yx')
        s = s.replace('yx','')
        res += s.count('xy')
    print(res)    