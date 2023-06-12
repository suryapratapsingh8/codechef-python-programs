# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    a=x-y
    print(min(a,y))