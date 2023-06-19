# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    u = input()
    sc = [0 if u[i] == 'N' else 1 if u[i] == s[i] else 0 if i == n-1 else -1 for i in range(n)]
    #print(sc)
    for i in range(n-1):
        if sc[i] == -1:
            sc[i] = 0
            sc[i+1] = 0
    #print(sc)
    print(sum(sc))