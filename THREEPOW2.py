# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    cnt=s.count('1')
    if s=='1' or s=='10':
        print("NO")
    elif cnt<=3:
        print("YES")
    else:
        print("NO")