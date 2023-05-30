# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    x=s.count('1')
    y=s.count('0')
    if n&1:
        print("YES")
        continue
    else:
        if x&1 and x!=y:
            print("NO")
            continue
        else:
            print("YES")
            continue