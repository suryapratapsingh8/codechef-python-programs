# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    print('CHEF' if sum(a)%2 or 1 in a else 'CHEFINA')