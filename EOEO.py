
# cook your dish here
for i in range(int(input())):
    n=int(input())
    cs=2
    while n%cs==0:
        cs*=2
    print(n//cs)