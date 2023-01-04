import math

for i in range(int(input())):  # For TestCases
    # Write code here
    l=list(map(int,input().split()))
    l.sort()
    
    if l[0]==l[3]:
        print(0)
    elif(l[0]==l[2] or l[1]==l[3]):
        print(1)
    else:
        print(2)

