import math
# cook your dish here
T = int(input())
for i in range(T):
    B, LS = map(int, input().split())
    min_RS = math.sqrt(LS**2- B**2)
    max_RS = math.sqrt(LS**2+ B**2)
    print(min_RS, max_RS)