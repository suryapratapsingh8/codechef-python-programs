# cook your dish here
for t in range(int(input())):
    a,b=map(int, input().split())
    if (b-a)>=2 and a%2==0:
        print(a,a+2)
    elif (b-a)>=3 and a%3==0:
        print(a,a+3)
    elif (b-a)>=3 and a%3!=0:
        print(a+1,a+3)
    else:
        print("-1")
