for _ in range(int(input())):
    n = int(input())
    a = [int(x) for x in input().split()] 
    maxa, mina = a[0], a[0]
    ans = "YES"
    for i in range(1, n):
        if a[i] >= maxa:
            maxa = a[i]
        elif a[i] <= mina:
            mina=a[i]
        else:
            ans = "NO"
            break
    print(ans)