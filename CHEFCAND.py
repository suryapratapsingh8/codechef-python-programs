# cook your dish here
for i in range(int(input())):
    children, candy = map(int, input().split(" "))
    remaining = children - candy
    if(remaining>0):
        if(remaining%4 == 0):
            print(remaining//4)
        else:
            print(remaining//4 +1)
    else:
        print(0)