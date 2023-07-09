# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=[int(x) for x in input().split()]
    d=x*y
    if x*y<=z:
        print("yes")
    else:
        print("no")