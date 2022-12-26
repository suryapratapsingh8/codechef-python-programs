T = int(input())
for i in range(T):
    N = int(input())
    strings = []
    for j in range(N):
        S = input()
        strings.append(S)
    if "cakewalk" in strings and "simple" in strings and "easy" in strings and ("easy-medium" in strings or "medium" in strings) and ("medium-hard" in strings or "hard" in strings):
        print("Yes")
    else:
        print("No")