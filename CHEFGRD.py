# cook your dish here
for i in range (int(input())):
    n,x,y=map(int,input().split())
    if (x+y)%2==0:
        print(0)
    else:
        print(1)