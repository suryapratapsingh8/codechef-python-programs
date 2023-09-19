a=[1]
for _ in range(1,31):
    a.append(a[_-1]*2)
for _ in range(int(input())):
    n=int(input())
    x=1
    if(n<4):
        print(3-n)
        continue
    for i in range(31):
        if(n<=a[i]):
            x=i
            break
    y=[]
    m=n
    y.append(abs(n-a[x]-1))
    n-=a[x-1]
    z=1
    for i in range(31):
        if(n<=a[i]):
            z=i
            break
    if(x-1!=z):
        y.append(abs(m-a[x-1]-a[z]))
    if(x-1!=z+1):
        y.append(abs(m-a[x-1]-a[z+1]))
    if(x!=z):
        y.append(abs(m-a[x-1]-a[z-1]))
    print(min(y))