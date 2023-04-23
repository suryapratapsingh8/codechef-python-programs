# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    p=s.count('1')
    y=(p*(p-1)//2)
    print(y+p)