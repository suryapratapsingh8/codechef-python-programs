# cook your dish here
for _ in range(int(input())):
    s = input()
    holy = [ 'A', 'B', 'D', 'O', 'P', 'Q', 'R']
    holes = 0
    for l in s:
        if l in holy:
            if l == 'B':
                holes += 2
            else:
                holes += 1
    else:
        print(holes)