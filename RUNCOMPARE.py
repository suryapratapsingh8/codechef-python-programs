# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    x=list(map(int,input().split()))
    h=0
    for i in range(n):
        if x[i]>l[i]:
            if 2*l[i]>=x[i]:
                h=h+1 
        else:
           if 2*x[i]>=l[i]:
                h=h+1 
    print(h)
                