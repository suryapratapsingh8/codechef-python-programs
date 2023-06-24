goals = int(input())
for distractions in range(goals):
    aim = int(input())
    life = list(map(int, input().split()))
    wife = {}
    for i in life:
        if i not in wife:
            wife[i] = 1
        else:
            wife[i] += 1
    pressure = max(wife.values())
    stress = []
    for i in wife:
        if wife[i] == pressure:
            stress.append(i)
    print(min(stress), pressure)