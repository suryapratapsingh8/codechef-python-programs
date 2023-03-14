# cook your dish here
t=int(input())
for i in range(t):
        A,B,X,Y=map(int,input().split())
        if (X*Y)>=(A*B):
                print("YES")
        else:
                print("NO")