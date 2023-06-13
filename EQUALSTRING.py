# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    seq = []
    match = []
    for i in range(n):
        if a[i] == b[i]:
            seq.append(1)
        else:
            seq.append(0)
            match.append(b[i])
    else:
        print(seq.count(0)- len(match) + len(set(match)))