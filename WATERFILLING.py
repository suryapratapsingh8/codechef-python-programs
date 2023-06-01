# cook your dish here
for _ in range(int(input())):
    a,b,c=map(int,input().split())
    if a==1 and b==1 or a==1 and c==1 or b==1 and c==1:
        print('Not now')
    else:
        print('Water filling time')
