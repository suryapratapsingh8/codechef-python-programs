for i in range(int(input())):
    x,y,z=map(int,input().split())
    n = (x//y+1)*y
    if y%z==0:
        print(-1)
    else:
        print( n if n%z!=0 else n+y)
            