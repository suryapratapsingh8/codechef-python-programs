
t=int(input())
for t in range(t):
    a,b,c=map(int,input().split())
    if(a<=b and c<=b):
        print("yes")
    else:
        print("no")