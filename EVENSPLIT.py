# cook your dish here
for _ in range(int(input())):
    n=int(input())
    l=input()
    a=l.count('0')
    d=n-a
    if n<3:
        print(l)
    else:
       
       print('0'*a + '1'*d)
