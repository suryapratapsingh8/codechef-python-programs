# cook your dish here
for _ in range(int(input())):
    p,x,y,z=map(int,input().split())
    if z==1:
        print(p+p*(y/100))
    else:
        print(p-p*(x/100))