# cook your dish here
for _ in range(int(input())):
    s = input()
    if s.count('1') == 0:
        print('NO')
        continue
    cnt1 = s.count('1')
    start = s.index('1')
    cnt0 = s[start:cnt1+start].count('0')
    print('NO' if cnt0 else 'YES')