t = int(input())
for i in range(t):
    x = input()
    y = input()
    for i in range(len(x)):
        if x[i]==y[i]:
            if x[i]=='W':
                print("B",end="")
            else:
                print("W",end="")
        else:
            print("B",end="")
    print()