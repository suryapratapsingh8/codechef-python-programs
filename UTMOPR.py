# cook your dish here
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = sum(list(map(int,input().split())))
    print('odd'  if a%2 == 0 and k == 1 else 'even')