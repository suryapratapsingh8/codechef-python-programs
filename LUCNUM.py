# cook your dish here
for _ in range(int(input())):
    n=int(input())
    c=0
    for i in range(n):
        if n&1!=0:
            break 
        else:

            n=n//2
            c=c+1 
    if c&1==0:
        print('1')
    else:
        print('0')