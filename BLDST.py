test = int(input())

for _ in range(test):
    Number, Member = map(int, input().split())
    Att = list(map(int, input().split()))

    Sum = sum([Number - Att[iter] for iter in range(Member)])

    print(max(0, Number - Sum))