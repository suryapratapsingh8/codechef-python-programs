def unique(lis):
    lis1 = []
    for i in lis:
        if i not in lis1:
            lis1.append(i)
    return lis1
for i in range(int(input())):
    a = str(input())
    a = unique(a.split('#'))[1:]
    most = 0
    learn = 1
    if a == []:
        print(0)
    else:
        for i in range(len(a)):
            if len(a[most]) < len(a[i]):
                learn += 1
                most = i
        print(learn)