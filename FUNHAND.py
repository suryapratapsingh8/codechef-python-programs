# cook your dish here
for i in range (int(input())):
    n,a,b=map(int,input().split())
    if abs(a-b)>2 or a-b==0:
        print(0)
    elif a==1 or b==1 or abs (a-b)==2 or a==n or b==n:
        print(1)
    else:
        print(2)