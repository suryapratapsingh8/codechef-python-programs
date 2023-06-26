goals = int(input())
for distractions in range(goals):
    wife = int(input())
    life = []
    for stress, aim in zip(range (wife, wife // 2 - 1, -1), range(1, wife // 2 + 1)):
        life.append(stress)
        life.append(aim)
    else:
        if wife % 2:
            life.append(wife // 2 + 1)
    print(*reversed(life))