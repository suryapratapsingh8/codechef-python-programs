def is_lapindrome(s):
    n = len(s)
    first_half = s[:n//2]
    second_half = s[n//2 + n%2:]
    return sorted(first_half) == sorted(second_half)

T = int(input())
for _ in range(T):
    s = input()
    if is_lapindrome(s):
        print("YES")
    else:
        print("NO")
