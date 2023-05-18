# cook your dish here
for _ in range(int(input())):
    a=int(input())
    if a&1==0 and a%7==0:
        print('Alice')
    elif a&1!=0 and a%9==0:
        print('Bob')
    else:
        print('Charlie')