# cook your dish here
for _ in range(int(input())):
    n=int(input())
    if n<6:
        print(0)
    else:
        k=n-6
        print((k//7)+1)