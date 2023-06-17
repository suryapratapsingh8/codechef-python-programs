# cook your dish here
for _ in range(int(input())):
    abc = list(map(int,input().split()))
    print('YES' if abc.count(min(abc)) >= 2 else 'NO')