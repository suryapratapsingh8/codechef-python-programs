T = int(input())

for _ in range(T):
    i = int(input())
    net = i
    tbp = 0
    if 250000 < i:
        f = i // 250000
        for j in range(f):
            net -= 250000 * tbp
            tbp += 0.05
            if tbp == 0.30:
                break
        net -= ((i - 250000 * (j+1)) * tbp)
    else:
        net = i
    print(int(net))
    