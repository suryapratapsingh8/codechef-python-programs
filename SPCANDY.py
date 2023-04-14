# cook your dish here
for _ in range(int(input())):
        x,y = map(int,input().split(' '))
        if y>0:
            print(x//y,x%y)
        else:
            print(0,x)