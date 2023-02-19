# cook your dish here
for i in range(int(input())):
    n=int(input())
    s=input()
    b=s[n-1:]
    a=s[:n-1]
    
    if(b in a):
        print('YES')
    else:
        print('NO')
    