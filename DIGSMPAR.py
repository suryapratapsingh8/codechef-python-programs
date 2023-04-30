# cook your dish here
def digitsum(n,p):
    s=0
    num=n
    while n!=0:
        s=s+(n%10)
        n=n//10
    if s%2 == p:
        return digitsum(num+1,p)
    else:
        return num
t=int(input())
for i in range(0,t):
    n=int(input())
    num=n
    s=0;p=0
    while n!=0:
        s=s+(n%10)
        n=n//10
    if s%2==1:
        p=1
    num+=1
    print(digitsum(num,p))