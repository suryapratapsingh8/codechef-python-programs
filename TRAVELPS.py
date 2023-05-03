# cook your dish here
t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    s = input()
    g = s.count('1')
    m = s.count('0')
    print((g*b)+(m*a))