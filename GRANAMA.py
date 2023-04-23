# cook your dish here
t = int(input())
for i in range(t):
    r,s = list(input().split())
    r_set = set(r)
    s_set = set(s)
    res = 'YES'
    if r_set == s_set:
        for i in r_set:
            if r.count(i)!=s.count(i):
                res='NO'
    print(res)