# cook your dish here
for i in range(int(input())):
    n = int(input())
    s = input()
    s = s.replace('010','xxx')
    s = s.replace('01','xx')
    s = s.replace('10','xx')
    print(s.count('0'))