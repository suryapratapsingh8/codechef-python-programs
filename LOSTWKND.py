# cook your dish here
for i in range(int(input())):
    a,b,c,d,e,p=map(int,input().split())
    x=(a+b+c+d+e)
    s=x*p
    if(s<=120):
        print("No")
    else:
        print("Yes")