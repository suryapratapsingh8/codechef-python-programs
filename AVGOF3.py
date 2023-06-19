goals = int(input())
for distractions in range(goals):
    wife = int(input())
    aim = wife * 3
    stress = 0
    for i in range(1, aim):
        for j in range(i + 1, aim):
            for k in range(j + 1, aim):
                if i + j + k == aim:
                    print(i, j, k)
                    stress = 1
                    break
            if stress == 1:
                break
        if stress == 1:
            break