# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n==1:
        print('no')
    elif n==2:
        print('yes')
    else:
        c=1
        for i in range(2,n//2):
            if n%i==0:
                c=0
        if c==0:
            print('no')
        else:
            print('yes')
                