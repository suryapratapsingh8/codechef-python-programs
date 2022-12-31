# The two dishes
for _ in range(int(input())):
    n,s=map(int,input().split())
    if n>=s:
        print(s)
    elif n<s:
       y=s-n
       print(n-y)
