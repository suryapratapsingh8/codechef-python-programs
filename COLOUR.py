t = int(input())
for i in range(t):
    x,y,z = map(int,input().split())
    if x>1 and y>1 and z>1:
        if x==2 and y==2 and z==2:
            print(4)
        elif x==2 or y==2 or z==2:
            print(5)
        else:
            print(6)
    elif (x>1 and y>1)or(y>1 and z>1)or(x>1 and z>1):
        if min(x,y,z)==0:
            print(3)
        else:
            print(4)
    elif x==y and x==z:
        print(x*3)
    elif (x==1 and y==1)or(y==1 and z==1)or(x==1 and z==1):
        if max(x,y,z)>1:
            print(3)
        else:
            print(2)
    elif x==1 or y==1 or z==1:
        if max(x,y,z)>1:
            print(2)
        else:
            print(1)
    else:
        print(1)

    