# cook your dish here
for _ in range (int(input())):
    n=int(input())
    s=input()
    c=s.count('1')
    print('0'*(n-c)+'1'*c)