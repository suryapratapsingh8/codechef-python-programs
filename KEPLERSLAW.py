# cook your dish here
for _ in range(int(input())):
    a,b,c,d=map(int,input().split())
    if (a*a)/(c*c*c)==(b*b)/(d*d*d):
        print('Yes')
    else:
        print('No')