# cook your dish here
for _ in range(int(input())):
    r,c=map(int,input().split())
    a=r*c
    if a%2==0:
        print("Yes")
    else:
        print("No")