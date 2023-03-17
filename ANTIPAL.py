# cook your dish here
for _ in range(int(input())):
    n=int(input())
    k=n//2
    if n&1!=0:
        print('-1')
    else:
        print('1'*k+'0'*k)