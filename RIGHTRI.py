# cook your dish here
count=0
for i in range(int(input())):
    x1,y1,x2,y2,x3,y3=map(int,input().split())
    a=(abs(x2-x1)**2) + (abs(y2-y1)**2)
    b=(abs(x3-x2)**2) + (abs(y3-y2)**2)
    c=(abs(x3-x1)**2) + (abs(y3-y1)**2)
    if a+b==c or b+c==a or c+a==b:
        count=count+1
print(count)