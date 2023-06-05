# cook your dish here

t=int(input())
for _ in range (t):
    U,V,A,S=map(int,input().split())
    if U==V:
        print("Yes")
    else:
        v=(U*U)-(2*A*S)
        if v<=V**2:
            print("Yes")
        else:
            print("No")