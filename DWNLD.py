# cook your dish here
T = int(input())
for i in range(T):
    (n,k) = map(int, input().split())
    amount = 0
    free = k
    for z in range(n):
        (t,d) = map(int, input().split())
        if free <= 0:
            amount += t*d
        else:
            if t-free < 0:
                free -= t
            else:
                amount += (t-free)*d
                free -= t
    print(amount)            