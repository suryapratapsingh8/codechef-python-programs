# cook your dish here
n = int(input())
for _ in range(n):
    x = int(input())
    if(x%10 == 0):
        print(0)
    elif(x%5==0):
        print(1)
    else:
        print(-1)