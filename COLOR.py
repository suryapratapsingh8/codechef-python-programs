# cook your dish here
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    s = Counter(input())
    print(n-s.most_common(1)[0][1])