t=int(input())
for i in range(t):
    n=int(input())
    list1=list(input().split())
    a=list1.count('A')
    b=list1.count('B')
    c=list1.count('AB')
    d=list1.count('O')
    if(a>=b):
        print(a+c+d)
    else:
        print(b+c+d)