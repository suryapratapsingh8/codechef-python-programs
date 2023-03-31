# cook your dish here
for i in range(int(input())):
    A,X,B,Y=map(int,input().split())
    if A/X > B/Y:
        print("ALICE")
    elif  A/X == B/Y:
        print("EQUAL")
    else:
        print("BOB")