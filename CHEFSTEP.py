for i in range(int(input())):
    n , k = map(int,input().split())
    a = list(map(int,input().split()))
    s = ''
    for i in a:
        if i % k == 0:
            s = s + '1'
        else:
            s = s + '0'
    print(s)