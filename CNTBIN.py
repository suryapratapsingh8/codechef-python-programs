# cook your dish here
for _ in range(int(input())):
    m=1000000007
    n=int(input())
    s=input()
    c=0
    ans=0
    for i in s:
        if i=='0':
            c=c+1 
        else:
            ans=ans+c
    print(ans%m)
        