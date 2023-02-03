
n=int(input())
s=input()

for k in range(n-1):
    p=input()
    d=""
    for i in s:
        if i in d:
            continue
        k1=s.count(i)
        k2=p.count(i)
        d=d+i*min(k1,k2)
    s=d
if s=="":
    print("no such string")
else:
    print(''.join(sorted(s)))