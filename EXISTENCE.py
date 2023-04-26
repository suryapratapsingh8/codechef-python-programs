# cook your dish here
t=int(input())
for i in range(t):
    x,y=[int(q) for q in input().split()]
    lhs=pow(x,4)+4*y**2
    rhs=4*x**2*y
    if lhs==rhs:
        print("YES")
    else:
        print("NO")