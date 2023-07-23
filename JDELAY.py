# cook your dish here
t=int(input())
for j in range(t):
    c=0
    n=int(input())
    for i in range(n):
        si,ji=map(int,input().split())
        if(abs(ji-si)>5):
            c=c+1
    print(c)