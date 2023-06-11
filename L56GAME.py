for i in range(int(input())):
    input()
    sequence = tuple(map(int, input().split()))
    if len(sequence) == 1:
        print(1)
    else:
        odds = 0
        for i in sequence:
            if i%2 == 1:
                odds += 1
        print(odds%2 + 1)