# cook your dish here
for i in range(int(input())):
    n=int(input())
    if n>=4:
        for i in range(n):
            if i==0:
                print("1",end="")
            elif i==1:
                print("0",end="")
            elif i==n-1:
                print("1",end="")
            elif i==n-2:
                print("0",end="")
            else:
                print("0",end="")
        print("")
    elif n==3:
        print("010")
    else:
        print("11")
