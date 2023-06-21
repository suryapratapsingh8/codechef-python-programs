goals = int(input())
for distractions in range(goals):
    wife, aim = map(int, input().split())
    life = list(map(int, input().split()))
    if sum(life) <= aim:
        print('Yes')
    else:
        print('No')