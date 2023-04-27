for _ in range(int(input())):
    n, b, m = map(int, input().split())
    x = list(map(int, input().split()))
    cache_block, count = -1, 0

    for i in x:
        block = i // b
        if cache_block != block:
            count += 1
            cache_block = block

    print(count)