# cook your dish here
for _ in range(int(input())):
    x,y,z=map(int,input().split())
    k=x+y+z 
    if k>=6:
        print('Yes')
    else:
        print('No')