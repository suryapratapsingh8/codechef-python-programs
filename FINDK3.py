# cook your dish here
post=int(input())
for p in range(post):
    a , b , c = map(int,input().split())
    if (b * c) % a == 0:
        print((b*c) , a)
    elif (a*b) % c == 0:
        print((a*b) , c)
    elif (a*c) % b == 0:
        print((a*c) , b)
    else:
        print(-1)