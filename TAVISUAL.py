for _ in range(int(input())):
    n, c, q = map(int, input().split()) 
    for t in range(q):
        a, b = map(int, input().split()) 
        if c >= a and c <= b:
            c = b-(c-a)
    print(c)
