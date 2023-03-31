# cook your dish here
for i in range(int(input())):
        a,b,x,y=map(int,input().split())
        if(a/b<x/y):
                print("Chef")
        elif(a/b>x/y):
                print("Chefina")
        else:
                print("Both")