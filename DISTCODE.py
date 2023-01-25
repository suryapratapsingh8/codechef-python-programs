t=int(input())
for i in range(t):
    s=input()
    c=set()
    for i in range(len(s)-1):
        c.add(s[i]+s[i+1])
    print(len(c)) 