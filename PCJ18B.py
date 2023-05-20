# cook your dish here
t=int(input())
for i in range(t):
    a=int(input())
    count=0
    while(a>0):
        count+=a*a
        a-=2
    print(count)
            