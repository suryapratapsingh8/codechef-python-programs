from math import gcd
goals = int(input())
for distractions in range(goals):
    wife, life = map(int, input().split())
    print(life // gcd(wife, life))