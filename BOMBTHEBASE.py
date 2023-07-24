for _ in range(int(input())):
    x,y=map(int,input().split())
    a=list(map(int,input().split()))
    count=0
    for i in range(x):
        if (a[i]<y):
            count=i+1
    print(count)
    