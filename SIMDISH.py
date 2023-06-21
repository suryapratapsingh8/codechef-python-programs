for _ in range(int(input())):
    first = input().split(' ')
    second = input().split(' ')
    cnt = 0
    for i in first:
        if i in second:
            cnt += 1 
    if cnt > 1:
        print('similar')
    else:
        print('dissimilar')