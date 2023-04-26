veda_t = int(input())

while veda_t > 0:
    veda_n = int(input())
    if veda_n % 10 >= 5:
        veda_n = veda_n + (10 - veda_n % 10)
    else:
        veda_n = veda_n - (veda_n % 10)
    print(100 - veda_n)
    veda_t -= 1

    