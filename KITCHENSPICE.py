for i in range(int(input())):
    n=int(input())
    if(n<4):
        print("MILD")
    elif(n>=4 and n<7):
        print("MEDIUM")
    else:
        print("HOT")