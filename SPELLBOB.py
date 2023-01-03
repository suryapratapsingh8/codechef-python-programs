# spell bob
for _ in range(int(input())):
    x=list(input())
    y=list(input())
    if (x[0]=='b' or y[0]=='b') and (x[1]=='o' or y[1]=='o') and (x[2]=='b' or y[2]=='b'):
        print("yes")
    elif (x[0]=='o' or y[0]=='o') and (x[1]=='b' or y[1]=='b') and (x[2]=='b' or y[2]=='b'):
        print("yes")
    elif (x[0]=='b' or y[0]=='b') and (x[1]=='b' or y[1]=='b') and (x[2]=='o' or y[2]=='o'):
        print("yes")
    else:
        print("no")