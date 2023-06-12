# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = list(input())
    rs = list(reversed(s))
    cnt = 0
    for let in rs:
        if not s:
            break
        if let == s[-1]:
            cnt += 1
            s.pop()
        if s:
            if let == s[-1]:
                s.pop()
            else:
                continue
    else:
        pass
    print(cnt)
    