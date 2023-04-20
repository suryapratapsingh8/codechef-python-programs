# cook your dish here
t = int(input())
for _ in range(t):
    line  = input()
    words = line.split()
    n = int(words[0])
    m = int(words[1])
    a = (n // 2) * (m // 2)
    print(n * m - a * 4)