# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    for i in a:
        if i%2 == 0:
            print('No')
            break
    else:
        print('Yes')
            